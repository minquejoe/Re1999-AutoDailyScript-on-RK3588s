import time
import logging
from adbutils import AdbDevice, AdbClient
import config

logger = logging.getLogger(__name__)

try:
    adb = AdbClient(host=config.adb_host, port=config.adb_port)
    adb.connect(config.device_serial)
    device = AdbDevice(adb, config.device_serial)
except Exception as e:
    logger.error("Failed to connect to ADB device: %s", e)
    raise


def game_one_tap(x: int, y: int) -> None:
    device.shell(f'input tap {x} {y}')


def game_go_back() -> None:
    device.shell('input keyevent BACK')


def game_double_tap(x: int, y: int) -> None:
    game_one_tap(x, y)
    time.sleep(config.double_tap_interval)
    game_one_tap(x, y)


def game_go_back_then_double_tap(x: int, y: int) -> None:
    game_go_back()
    time.sleep(config.go_back_sleep_time)
    game_double_tap(x, y)


def game_tap_sleep_short(x1: int, y1: int, x2: int, y2: int) -> None:
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)


def game_sleep_tap_long(x1: int, y1: int, x2: int, y2: int) -> None:
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_long_interval)
    game_one_tap(x2, y2)


def game_one_tap_long_sleep(x: int, y: int) -> None:
    game_one_tap(x, y)
    time.sleep(config.long_sleep)


def game_daily_weekly_tap(x1: int, y1: int, x2: int, y2: int) -> None:
    game_one_tap(x1, y1)
    time.sleep(config.sleep_tap_short_interval)
    game_go_back()
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x2, y2)
    time.sleep(config.sleep_tap_short_interval)
    game_one_tap(x1, y1)
    game_go_back()
    game_go_back()


def game_juke_tap(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> None:
    game_tap_sleep_short(x1, y1, x2, y2)
    game_tap_sleep_short(x3, y3, x1, y1)


def game_start() -> None:
    device.shell(f'am start -n {config.package_name}/{config.start_activity_name}')


def game_close() -> None:
    device.shell(f'am force-stop {config.package_name}')


def take_screenshot() -> None:
    pilimg = device.screenshot()
    if pilimg is None:
        raise RuntimeError("Screenshot returned None - device may be disconnected")
    pilimg.save(config.IMG_PATH)
