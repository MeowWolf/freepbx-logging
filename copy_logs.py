import os
import shutil
from datetime import datetime

log_directory = "/var/log/asterisk/"

def find_log_file(log_directory, target_date):
    target_filename = "full-{}".format(target_date.strftime('%Y%m%d'))
    full_path = os.path.join(log_directory, target_filename)

    if os.path.exists(full_path):
        return full_path
    else:
        return None


# Get the current date
current_date = datetime.now().date()

found_file = find_log_file(log_directory, current_date)
dest_path = '/home/mwdevops/json/full/'

if found_file:
    #print("Log file found: " + found_file)
    shutil.copy(found_file, dest_path)
    print("Successfully copied {} to {}".format(found_file, dest_path))

else:
    print("Log file not found for the current date.")