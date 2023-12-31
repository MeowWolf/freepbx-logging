import json
import re
import shutil
import requests
import os

#Function 1 Pull /var/log/asterisk.log file
def full_log_copy():
    src_path = r'/var/log/asterisk/full'
    dest_path = r'/home/mwdevops/json/full'
    shutil.copy(src_path, dest_path)


full_log_copy()
'''
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
    parse_log_file("/mwdevops/home/JSON/freepbx/freepbx.log")
    parse_log_line()
    log_file_path = "/mwdevops/home/JSON/freebpx/freepbx.log"
    log_entries = parse_log_file(log_file_path)

    # Convert the list of log entries to JSON
    log_json = json.dumps(log_entries, indent=4)

    # Save the JSON to a file or print it
    with open("freepbx_output.json", "w") as json_file:
        json_file.write(log_json)

#converts system log file from a bove into JSON format (saves file in .json)
def convert_system_log():
    parse_log_file("/mwdevops/home/JSON/system/system.log")
    log_file_path = "/mwdevops/home/JSON/system/system.log"
    log_entries = parse_log_file(log_file_path)

    # Convert the list of log entries to JSON
    log_json = json.dumps(log_entries, indent=4)

    # Save the JSON to a file or print it
    with open("system_output.json", "w") as json_file:
        json_file.write(log_json)

#copy the stuff from the next file over here
'''
'''def send_asterisk_json():
    os.chdir('/mwdevops/home/json/asterisk/')
    headers = {
        'Content-type': 'application/json'
               }
    r = requests.post('https://302d63369ddc4072852f17a5a7b7771e.us-central1.gcp.cloud.es.io:443/search-twilio-english/_doc?pipeline=ent-search-generic-ingestion')'''
'''
#convert each line of JSON to its own file
# List of items you want to make POST requests for
def send_freepbx_logs():
    items = []

# URL where you want to make the POST requests
    url = 'http://34.174.243.169:8080'

# Iterate through the items and make POST requests
    for item in items:
        data = {'item': item}  # You can adjust the payload data as needed
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(f"Successfully made POST request for {item}")
        else:
            print(f"Failed to make POST request for {item}. Status code: {response.status_code}")

#def send_system_logs():
#    items = 

# URL where you want to make the POST requests
    url = 'http://34.174.243.169:8080'

# Iterate through the items and make POST requests
    for item in items:
        data = {'item': item}  # You can adjust the payload data as needed
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(f"Successfully made POST request for {item}")
        else:
            print(f"Failed to make POST request for {item}. Status code: {response.status_code}")
'''
