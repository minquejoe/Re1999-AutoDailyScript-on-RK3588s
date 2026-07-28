import logging
import os
import shutil
import time
from datetime import datetime

import config
from adb_driver import game_go_back
from inference import once_infer

logger = logging.getLogger(__name__)


def save_pic(pic_save_flag: bool) -> None:
    if not pic_save_flag:
        logger.debug("Pic saving disabled (PIC_SAVE_FLAG=False)")
        return

    num_pics = len([
        name for name in os.listdir(config.PIC_SAVE_PATH)
        if os.path.isfile(os.path.join(config.PIC_SAVE_PATH, name))
    ])

    if num_pics < config.PIC_SAVE_MAX:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_name = f"screenshot{timestamp}.jpg"
        shutil.move(config.IMG_PATH, os.path.join(config.PIC_SAVE_PATH, new_name))
        logger.info("Saved screenshot: %s", new_name)
    else:
        logger.warning("Max pics reached (%d), not saving", config.PIC_SAVE_MAX)


class OrderChecker:
    """Detects out-of-order scene transitions during task execution."""

    def __init__(self, class_order: list[str]) -> None:
        self._order_map = {name: idx for idx, name in enumerate(class_order)}
        self._current_index: int | None = None

    def check(self, class_name: str) -> None:
        if class_name not in self._order_map:
            return

        new_index = self._order_map[class_name]
        if self._current_index is not None:
            expected = self._current_index + 1
            if new_index != self._current_index and new_index != expected:
                logger.warning("Out-of-order detected: '%s' (expected index %d, got %d)",
                               class_name, expected, new_index)
                save_pic(config.PIC_SAVE_FLAG)

        self._current_index = new_index


def to_task(class_to_adb: dict, finish_class: list[str], class_order: list[str]) -> None:
    order_checker = OrderChecker(class_order)

    while True:
        scores, idx_sorted, labels = once_infer()
        output = labels[idx_sorted[0]]
        class_name = output.split()[-1].strip()
        confidence = scores[idx_sorted[0]]

        logger.info("Recognition: P %.2f LABEL %s", confidence, output)
        order_checker.check(class_name)

        if class_name == "waiting":
            logger.info("Waiting... sleeping %ds", config.next_task_interval)
            time.sleep(config.next_task_interval)
            continue

        if class_name not in class_to_adb or class_name in ("others", "battle_ongoing"):
            logger.info("Undefined or skipped class: %s - going back", class_name)
            save_pic(config.PIC_SAVE_FLAG)
            game_go_back()
            time.sleep(config.next_task_interval)
            continue

        entry = class_to_adb[class_name]
        func = entry['func']
        params = entry['params']
        logger.info("Executing: %s(%s)", func.__name__, params)
        func(**params)

        if class_name in finish_class:
            logger.info("Task finished")
            break

        time.sleep(config.next_task_interval)
