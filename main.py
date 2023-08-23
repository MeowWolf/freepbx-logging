import json
import re
import shutil
import requests
import os
import subprocess
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv()

HEADERS = {'Content-Type': 'application/json'}

URL = os.getenv('URL')
parse_file = os.getenv('PARSE_FILE')
log_directory = os.getenv('LOG_DIR')
dest_directory = os.getenv('DEST_DIR')

# 
current_date = datetime.now().date()


def log_copy(log_dir, target_date):
    target_file = "full-{}".format(target_date.strftime('%Y%m%d'))
    full_path = os.path.join(log_dir, target_file)

    if os.path.exists(full_path):
        shutil.copy(full_path, dest_path)
    else:
        print("Log file not found")

def parse_log_line(log_line):

    log_pattern = r'\[(.*?)\] (\w+)\[(\d+)\] (.+?): (.*)'
    match = re.match(log_pattern, log_line)

    if match:
        timestamp = match.group(1)
        level = match.group(2)
        process_id= match.group(3)
        source = match.group(4)
        message = match.group(5)    
        return timestamp, level, process_id, source, message

    else: 
        return None, None, None, None, None

def parse_log_file(log_folder_path):
    log_entries = []

    log_files = [file for file in os.listdir(log_folder_path) if file.startswitch('full-')]
    sorted_log_files = sorted(log_files, key=lambda x: x.split('-')[-1])

    latest_log_file = sorted_log_files[-1]

    with open(os.path.join(log_folder_path, latest_log_file), 'r') as log_file:
        for line in log_file:
            timestamp, level, process_id, source, message = parse_log_line(line)

            log_entry = {
                "timestamp": timestamp,
                "level": level,
                "process_id": process_id,
                "source": source,
                "message": message
            }

            if log_entry["level"] == "VERBOSE" or log_entry["level"] == None:
                pass

            else:
                log_entries.append(log_entry)
                latest_timestamp = timestamp

    return log_entries, latest_timestamp


def send_full_logs():

    with open("log_output.json", "r") as file:
        json_data_list = json.load(file)

        for item in json_data_list:
            response = requests.post(URL, headers=HEADERS, json=item)
            if response.status_code == 200:
                print(f"Sucess {item}")
            else:
                print(f"Failed POST for {item}. Status code: {response.status_code}")

def send_log(entry):
    print("Adding new log \n")

    print(entry)
    #response = requests.port(URL, header=HEADERS, j)

def main():
    while True:
        log_copy(log_directory, current_date)

        log_entries, latest_timestamp = parse_log_file(parse_file)

        log_json = json.dumps(log_entries, indent=4)

        with open("log_output.json", "w") as json_file:
            json_file.write(log_json)

        for entry in log_entries:
            if entry['timestamp'] > latest_timestamp:
                send_log(entry)
                filtered_entries.append(entry)
            else:
                filtered_entries = log_entries


        time.sleep(30) 

if __name__ == "__main__":
    main()


