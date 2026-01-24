# 包含<识别出的场景>对应的<需要点击的位置>
# 相同的<识别出的场景>在不同的文件里对应不同<需要点击的位置>

login_update = {'x':1165, 'y':655}
login_error = {'x':1200, 'y':700}
login_quit = {'x':1175, 'y':680}
waiting = {'x':1200, 'y':700}
menu = {
        'to_menu.py':{'x':1000, 'y':700},       # 菜单处与角色互动
        'to_harvest.py':{'x':1500, 'y':600},
        'to_mind.py':{'x':1600, 'y':450}, 
        'to_gold.py':{'x':1600, 'y':450}, 
        'to_dust.py':{'x':1600, 'y':450}, 
        'to_mailbox.py':{'x':115, 'y':280},
        'to_daily_weekly.py':{'x':120, 'y':400},
        # 'to_juke.py':{'x':325, 'y':110},        # icon第一位置，无装饰
        'to_juke.py':{'x':500, 'y':110},        # icon第一位置，有装饰
        # 'to_juke.py':{'x':440, 'y':100},        # icon第一位置，周年装饰
        }
menu_quit = menu

wilders_fullview = {'x':1040, 'y':295}
wilders_harvest = {'x1':1740, 'y1':330, 'x2':1740, 'y2':630}

battle_story = {'x':755, 'y':970}
battle_resource_01 = {
        'to_mind.py':{'x':550, 'y':525}, 
        'to_gold.py':{'x':1320, 'y':525},       # 识别不出 battle_resource_02 ，此处用 01 代替
        'to_dust.py':{'x':490, 'y':525},       # 识别不出 battle_resource_02 ，此处用 01 代替
        }
battle_resource_mind = {'x1':640, 'y1':900, 'x2':1600, 'y2':920}        # 识别不出意识、灰尘进入界面
battle_entry = battle_resource_mind     # 会把选择界面识别为进入界面
battle_confirm = {'x':1600, 'y':990}
battle_win = {'x':210, 'y':70}
levelup = {'x':210, 'y':70}

battle_resource_02 = battle_resource_01
battle_resource_gold = battle_resource_mind

battle_resource_dust = battle_resource_mind

mailbox = {'x':300, 'y':930}

task_daily = {'x1':1760, 'y1':240, 'x2':1660, 'y2':100}
task_weekly = task_daily

juke_box_calim = {'x1':1800, 'y1':1000, 'x2':1400, 'y2':60}
juke_box_point = juke_box_calim.copy()
juke_box_point.update({'x3':1400, 'y3':130})
juke_box_calim_finish = {'x':210, 'y':70}
