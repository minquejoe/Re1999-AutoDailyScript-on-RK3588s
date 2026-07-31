import logging
import signal
import time

import config
from adb_driver import game_start, game_close
from email_notifier import send_email
from run_task import run_task

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
)
logger = logging.getLogger(__name__)


class TaskTimeout(Exception):
    """Raised by signal handler when a task exceeds its time limit."""


def _timeout_handler(signum: int, frame) -> None:
    raise TaskTimeout()


def main() -> None:
    err_count = config.ERR_COUNT

    while err_count > 0:
        game_start()
        timed_out_tasks: list[str] = []

        for task_name in config.task_seq:
            old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(config.task_timeout)

            try:
                run_task(task_name)
            except TaskTimeout:
                timed_out_tasks.append(task_name)
                logger.error("Task '%s' timed out after %ds", task_name, config.task_timeout)
                game_close()
                game_start()
            except Exception as e:
                timed_out_tasks.append(task_name)
                logger.error("Task '%s' raised exception: %s", task_name, e)
            finally:
                signal.alarm(0)
                signal.signal(signal.SIGALRM, old_handler)

            logger.info("Next task in %ds...", config.next_file_interval)
            time.sleep(config.next_file_interval)

        if timed_out_tasks:
            send_email('\n'.join(timed_out_tasks))

        if len(timed_out_tasks) >= config.task_timeout_threshold:
            err_count -= 1
            logger.warning("Too many failures (%d/%d). Retries remaining: %d",
                           len(timed_out_tasks), config.task_timeout_threshold, err_count)
            time.sleep(config.seq_retry_wait)
        else:
            err_count = 0

        game_close()


if __name__ == '__main__':
    main()
