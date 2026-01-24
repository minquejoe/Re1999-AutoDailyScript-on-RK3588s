import os
from to_task import to_task
import config_positions
from utils import game_one_tap, game_double_tap, game_go_back_then_double_tap

# Define the mapping from class name to adb command
class_to_adb = {
    'menu': {'func': game_double_tap, 'params': config_positions.menu[os.path.basename(__file__)]},
    'mailbox': {'func': game_double_tap, 'params': config_positions.mailbox},
}

class_order = ["menu", "mail_box"]
finish_class = ["mail_box"]

print("*="*20)
print(f'|| trun game to -> {os.path.splitext(os.path.basename(__file__))[0]} ||')
to_task(class_to_adb, finish_class, class_order)
