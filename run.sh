#!/bin/bash
cd /home/orangepi/Re1999-AutoDailyScript-on-RK3588s
source /home/orangepi/miniconda3/bin/activate Re1999-AutoDailyScript
python run.py >> "/tmp/Re1999_$(date +%Y%m%d_%H%M%S).log" 2>&1
