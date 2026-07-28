import logging

import cv2
import numpy as np
from rknnlite.api import RKNNLite
from scipy.special import softmax

import config

logger = logging.getLogger(__name__)


class ModelManager:
    """Singleton that loads the RKNN model once and reuses it."""

    _instance: "ModelManager | None" = None

    def __new__(cls) -> "ModelManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self._initialized = True

        self.rknn = RKNNLite()

        ret = self.rknn.load_rknn(config.RKNN_MODEL)
        if ret != 0:
            raise RuntimeError(f"Failed to load RKNN model: {config.RKNN_MODEL}")

        ret = self.rknn.init_runtime(core_mask=RKNNLite.NPU_CORE_AUTO)
        if ret != 0:
            raise RuntimeError("Failed to initialize RKNN runtime")

        logger.info("RKNN model loaded successfully")

        with open(config.CLASS_LABEL_PATH, 'r') as f:
            self.labels = [line.rstrip() for line in f]

    def infer(self, image_path: str) -> tuple[np.ndarray, np.ndarray, list[str]]:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Failed to read image: {image_path}")
        img = cv2.resize(img, (config.MODEL_INPUT_SIZE, config.MODEL_INPUT_SIZE))
        img = np.expand_dims(img, 0)

        outputs = self.rknn.inference(inputs=[img])

        scores = softmax(outputs[0])
        scores = np.squeeze(scores)
        idx_sorted = np.argsort(scores)[::-1]

        return scores, idx_sorted, self.labels

    def release(self) -> None:
        if hasattr(self, 'rknn'):
            self.rknn.release()
            logger.info("RKNN model released")


def once_infer() -> tuple[np.ndarray, np.ndarray, list[str]]:
    from adb_driver import take_screenshot
    take_screenshot()
    model = ModelManager()
    return model.infer(config.IMG_PATH)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    scores, idx_sorted, labels = once_infer()
    for i in idx_sorted[0:5]:
        print('[%d] score=%.2f class="%s"' % (i, scores[i], labels[i]))
