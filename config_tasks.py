import config_positions as pos

CONFIG_TASKS: dict[str, dict] = {
    "menu": {
        "class_to_adb": {
            'login_update': {'func': 'game_double_tap', 'params': pos.login_update},
            'login_error': {'func': 'game_double_tap', 'params': pos.login_error},
            'login_quit': {'func': 'game_double_tap', 'params': pos.login_quit},
            'menu': {'func': 'game_double_tap', 'params': pos.menu['menu']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['menu']},
        },
        "class_order": ["waiting", "login_update", "menu"],
        "finish_class": ["menu", "menu_quit"],
    },
    "harvest": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['harvest']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['harvest']},
            'wilders_fullview': {'func': 'game_double_tap', 'params': pos.wilders_fullview},
            'wilders_harvest': {'func': 'game_sleep_tap_long', 'params': pos.wilders_harvest},
        },
        "class_order": ["menu", "wilders_fullview", "wilders_harvest"],
        "finish_class": ["wilders_harvest"],
    },
    "mind": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['mind']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['mind']},
            'battle_story': {'func': 'game_one_tap', 'params': pos.battle_story},
            'battle_resource_01': {'func': 'game_one_tap', 'params': pos.battle_resource_01['mind']},
            'battle_resource_mind': {'func': 'game_tap_sleep_short', 'params': pos.battle_resource_mind},
            'battle_entry': {'func': 'game_tap_sleep_short', 'params': pos.battle_entry},
            'battle_confirm': {'func': 'game_one_tap_long_sleep', 'params': pos.battle_confirm},
            'battle_win': {'func': 'game_go_back_then_double_tap', 'params': pos.battle_win},
            'levelup': {'func': 'game_one_tap', 'params': pos.levelup},
        },
        "class_order": [
            "menu", "battle_story", "battle_resource_01", "battle_resource_mind",
            "battle_entry", "battle_confirm", "battle_ongoing", "battle_win",
        ],
        "finish_class": ["battle_win"],
    },
    "gold": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['gold']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['gold']},
            'battle_story': {'func': 'game_one_tap', 'params': pos.battle_story},
            'battle_resource_01': {'func': 'game_one_tap', 'params': pos.battle_resource_01['gold']},
            'battle_resource_02': {'func': 'game_one_tap', 'params': pos.battle_resource_02},
            'battle_resource_gold': {'func': 'game_tap_sleep_short', 'params': pos.battle_resource_gold},
            'battle_entry': {'func': 'game_tap_sleep_short', 'params': pos.battle_entry},
            'battle_confirm': {'func': 'game_one_tap_long_sleep', 'params': pos.battle_confirm},
            'battle_win': {'func': 'game_go_back_then_double_tap', 'params': pos.battle_win},
            'levelup': {'func': 'game_one_tap', 'params': pos.levelup},
        },
        "class_order": [
            "menu", "battle_story", "battle_resource_01", "battle_resource_02",
            "battle_resource_gold", "battle_entry", "battle_confirm",
            "battle_ongoing", "battle_win",
        ],
        "finish_class": ["battle_win", "low_vitality"],
    },
    "dust": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['dust']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['dust']},
            'battle_story': {'func': 'game_one_tap', 'params': pos.battle_story},
            'battle_resource_01': {'func': 'game_one_tap', 'params': pos.battle_resource_01['dust']},
            'battle_resource_02': {'func': 'game_one_tap', 'params': pos.battle_resource_02},
            'battle_resource_dust': {'func': 'game_tap_sleep_short', 'params': pos.battle_resource_dust},
            'battle_entry': {'func': 'game_tap_sleep_short', 'params': pos.battle_entry},
            'battle_confirm': {'func': 'game_one_tap_long_sleep', 'params': pos.battle_confirm},
            'battle_win': {'func': 'game_go_back_then_double_tap', 'params': pos.battle_win},
            'levelup': {'func': 'game_one_tap', 'params': pos.levelup},
        },
        "class_order": [
            "menu", "battle_story", "battle_resource_01", "battle_resource_02",
            "battle_resource_dust", "battle_entry", "battle_confirm",
            "battle_ongoing", "battle_win",
        ],
        "finish_class": ["battle_win", "low_vitality"],
    },
    "mailbox": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['mailbox']},
            'mail_box': {'func': 'game_double_tap', 'params': pos.mailbox},
        },
        "class_order": ["menu", "mail_box"],
        "finish_class": ["mail_box"],
    },
    "daily_weekly": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['daily_weekly']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['daily_weekly']},
            'task_daily': {'func': 'game_daily_weekly_tap', 'params': pos.task_daily},
            'task_weekly': {'func': 'game_daily_weekly_tap', 'params': pos.task_weekly},
        },
        "class_order": ["menu", "task_daily", "task_weekly"],
        "finish_class": ["task_daily", "task_weekly"],
    },
    "juke": {
        "class_to_adb": {
            'menu': {'func': 'game_double_tap', 'params': pos.menu['juke']},
            'menu_quit': {'func': 'game_go_back_then_double_tap', 'params': pos.menu_quit['juke']},
            'juke_box_point': {'func': 'game_juke_tap', 'params': pos.juke_box_point},
            'juke_box_claim': {'func': 'game_tap_sleep_short', 'params': pos.juke_box_claim},
            'juke_box_claim_finish': {'func': 'game_one_tap', 'params': pos.juke_box_claim_finish},
        },
        "class_order": ["menu", "juke_box_point", "juke_box_claim", "juke_box_claim_finish"],
        "finish_class": ["juke_box_claim", "juke_box_claim_finish"],
    },
}
