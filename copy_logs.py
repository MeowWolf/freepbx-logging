import shutil

def full_log_copy():
    src_path = r'/var/log/asterisk/full'
    dest_path = r'/home/mwdevops/json/full'
    shutil.copy(src_path, dest_path)

full_log_copy()