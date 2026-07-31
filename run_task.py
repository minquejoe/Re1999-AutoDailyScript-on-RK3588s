import argparse
import importlib
import logging
import sys

from config_tasks import CONFIG_TASKS
from to_task import to_task

logger = logging.getLogger(__name__)

FUNCTION_MODULES = ['adb_driver']


def _resolve_function(func_name: str):
    for module_name in FUNCTION_MODULES:
        module = importlib.import_module(module_name)
        if hasattr(module, func_name):
            return getattr(module, func_name)
    raise AttributeError(f"Function '{func_name}' not found in modules: {FUNCTION_MODULES}")


def run_task(task_name: str) -> None:
    if task_name not in CONFIG_TASKS:
        logger.error("Unknown task: %s. Available: %s", task_name, list(CONFIG_TASKS.keys()))
        sys.exit(1)

    task_cfg = CONFIG_TASKS[task_name]
    class_to_adb = {}

    for class_name, entry in task_cfg["class_to_adb"].items():
        func = _resolve_function(entry["func"])
        class_to_adb[class_name] = {
            'func': func,
            'params': entry["params"],
        }

    logger.info("========== Running task: %s ==========", task_name)
    to_task(class_to_adb, task_cfg["finish_class"], task_cfg["class_order"])
    logger.info("========== Task finished: %s ==========", task_name)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    )

    parser = argparse.ArgumentParser(description="Run a Re1999 automation task")
    parser.add_argument("task", choices=list(CONFIG_TASKS.keys()), help="Task name to run")
    args = parser.parse_args()

    run_task(args.task)
