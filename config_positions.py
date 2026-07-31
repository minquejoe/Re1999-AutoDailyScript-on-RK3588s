# Position mappings: recognized scene -> tap coordinates
# Keys are task names matching config_tasks.CONFIG_TASKS

login_update = {'x': 1165, 'y': 655}
login_error = {'x': 1200, 'y': 700}
login_quit = {'x': 1175, 'y': 680}
waiting = {'x': 1200, 'y': 700}

# Menu positions per task (each task navigates to a different menu area)
menu = {
    'menu': {'x': 1000, 'y': 700},
    'harvest': {'x': 1500, 'y': 600},
    'mind': {'x': 1600, 'y': 450},
    'gold': {'x': 1600, 'y': 450},
    'dust': {'x': 1600, 'y': 450},
    'mailbox': {'x': 115, 'y': 280},
    'daily_weekly': {'x': 120, 'y': 400},
    # 'juke':{'x':325, 'y':110},        # icon第一位置，无装饰
    # 'juke':{'x':500, 'y':110},        # icon第一位置，有装饰
    'juke':{'x':440, 'y':100},        # icon第一位置，周年装饰
}
menu_quit = menu  # Quit positions same as menu positions

wilders_fullview = {'x': 1040, 'y': 295}
wilders_harvest = {'x1': 1740, 'y1': 330, 'x2': 1740, 'y2': 630}

battle_story = {'x': 755, 'y': 970}
battle_resource_01 = {
    'mind': {'x': 550, 'y': 525},
    'gold': {'x': 1320, 'y': 525},
    'dust': {'x': 490, 'y': 525},
}
battle_resource_mind = {'x1': 640, 'y1': 900, 'x2': 1600, 'y2': 920}
battle_entry = battle_resource_mind
battle_confirm = {'x': 1600, 'y': 990}
battle_win = {'x': 210, 'y': 70}
levelup = {'x': 210, 'y': 70}

battle_resource_02 = battle_resource_01
battle_resource_gold = battle_resource_mind
battle_resource_dust = battle_resource_mind

mailbox = {'x': 300, 'y': 930}

task_daily = {'x1': 1760, 'y1': 240, 'x2': 1660, 'y2': 100}
task_weekly = task_daily

juke_box_claim = {'x1': 1800, 'y1': 1000, 'x2': 1400, 'y2': 60}
juke_box_point = juke_box_claim.copy()
juke_box_point.update({'x3': 1400, 'y3': 130})
juke_box_claim_finish = {'x': 210, 'y': 70}
