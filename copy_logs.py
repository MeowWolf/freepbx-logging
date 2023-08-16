import shutil
import os
from datetime import datetime
import re

def find_latest_full_log():
    log_folder = '/var/log/asterisk'
    full_logs = [file for file in os.listdir(log_folder) if file.startswith('full-') and re.match(r'full-\d{4}/\d{2}/\d{2}$', file)]
    sorted_logs = sorted(full_logs, key=lambda x: datetime.strptime(x.split('-')[-1]))
    
    if sorted_logs:
        return os.path.join(log_folder, sorted_logs[0])
    else:
        return None

def full_log_copy():
    src_path = find_latest_full_log()
    dest_path = '/home/mwdevops/json/full/'
    
    if src_path:
        shutil.copy(src_path, dest_path)
        print(f"Successfully copied {src_path} to {dest_path}")
    else:
        print("No suitable log file found.")

full_log_copy()