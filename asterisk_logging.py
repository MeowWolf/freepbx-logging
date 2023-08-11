import json
import re
import shutil
import requests
import os
import subprocess

#Function calls the copy_logs.py script to run the script as sudo
def run_full_log_copy_as_sudo():
    #needs a command to cd to whatever directory we save copy_logs.py to
    #something like: 
    #change_directory = "/path/to/directory/file.py"
    #os.chdir(change_directory)
    #add a print statmement for testing to confirm the cd worked
    #print("New directory is:", os.getcwd())
    
    sudo_command = "sudo python3 copy_logs.py"
    
    try:
        subprocess.run(sudo_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Sudo command executed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error executing sudo command:", e)

#Parses log entries into a list item called log_entries
def parse_log_file(log_file_path):
    log_entries = []

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Parse the log line and extract relevant information
            timestamp, level, message = parse_log_line(line)

            # Create a dictionary for the log entry
            log_entry = {
                'timestamp': timestamp,
                'level': level,
                'message': message
            }

            log_entries.append(log_entry)

    return log_entries

#parses logs into the needed format (JSON)
def parse_log_line(log_line):
    # Define a regular expression pattern to match the log entry format
    log_pattern = r'\[(.*?)\] \[(.*?)\]: (.*)'
    match = re.match(log_pattern, log_line)

    if match:
        timestamp = match.group(1)
        level = match.group(2)
        message = match.group(3)
        return timestamp, level, message
    else:
        # Return default values or handle the case where the line doesn't match the format
        return None, None, None

#converts freepbx log file from above into JSON format (saves file in .json)
def convert_freepbx_log():
    parse_log_file("/home/mwdevops/json/full/full")
    parse_log_line()
    log_file_path = "/home/mwdevops/json/full/full"
    log_entries = parse_log_file(log_file_path)

    # Convert the list of log entries to JSON
    log_json = json.dumps(log_entries, indent=4)

    # Save the JSON to a file or print it
    with open("full_output.json", "w") as json_file:
        json_file.write(full_json)

#convert each line of JSON to its own file
# List of items you want to make POST requests for
def send_full_logs():
    items = []
    with open('full_output.json', 'r') as file:
        for line in file:
            items.append(line.strip())

        timestamp_keys = [key for key in items.keys() if re.match(r'timestamp\d+', key)]
        timestamp_values = [items[key] for key in timestamp_keys]
        sorted_timestamps = sorted(timestamp_values)
        global latest_timestamp = sorted_timestamps[-1]
        print("Latest Timestamp:", latest_timestamp)
# URL where you want to make the POST requests
    url = 'http://34.174.243.169:8080'  #depending on how much noise we can filter out it may be easier / make more sense to send data via ingest pipeline over LS

# Iterate through the items and make POST requests
    for item in items:
        data = {'item': item}  # You can adjust the payload data as needed
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(f"Successfully made POST request for {item}")
        else:
            print(f"Failed to make POST request for {item}. Status code: {response.status_code}")

def log_send_loop():
    global latest_timestamp
    run_full_log_copy_as_sudo()
    parse_log_file()
    parse_log_line()
    convert_freepbx_log()
    send_full_logs()