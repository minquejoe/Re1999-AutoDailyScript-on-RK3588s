# ==========================
#     ADB server and device
# ==========================
adb_host = "127.0.0.1"
adb_port = 5038
device_serial = "localhost:6602"

# ==========================
#         Game info
# ==========================
package_name = 'com.shenlan.m.reverse1999'
start_activity_name = 'com.ssgame.mobile.gamesdk.frame.AppStartUpActivity'

# ==========================
#     Interaction timing
# ==========================
double_tap_interval = 0.25
sleep_tap_long_interval = 10
sleep_tap_short_interval = 5
go_back_sleep_time = 3
next_task_interval = 5
next_file_interval = 5
long_sleep = 90

# ==========================
#        Task chain
# ==========================
ERR_COUNT = 3          # Max task chain retry count
seq_retry_wait = 30    # Seconds to wait before each retry
task_timeout = 300     # Seconds, per-task timeout
task_timeout_threshold = 5  # Max allowed task failures before chain retry

# Task names must match keys in task_configs.TASK_CONFIGS
task_seq = [
    "menu",
    "harvest",
    "menu",
    "mind",
    "menu",
    "gold",
    "menu",
    "dust",
    "mailbox",
    "menu",
    "harvest",
    "menu",
    "daily_weekly",
    "menu",
    "juke",
]

# ==========================
#      Email alert (SMTP)
# ==========================
SMTP_HOST = "smtp.qq.com"
SMTP_PORT = 465
SOURCE_MAIL_ADDR = "xxx"
SOURCE_MAIL_PASS = "xxx"
TARGET_MAIL_ADDR = SOURCE_MAIL_ADDR

# ==========================
#       MobileNet / RKNN
# ==========================
RKNN_MODEL = 'model/mobilenetv2_re1999.rknn'
IMG_PATH = './screenshot.jpg'
CLASS_LABEL_PATH = 'model/mobilenetv2_re1999_class_labels.txt'
MODEL_INPUT_SIZE = 224

# ==========================
#    Training data capture
# ==========================
PIC_SAVE_FLAG = False
PIC_SAVE_PATH = "screenShot"
PIC_SAVE_MAX = 100
