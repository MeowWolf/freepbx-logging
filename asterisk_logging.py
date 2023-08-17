import json
import re
import requests
import os
import subprocess

def run_shell_script():
    script_name = "change_file_perms.sh"
    subprocess.run(['./' + script_name, '&'], shell=True)
    print("ran")
#Function calls the copy_logs.py script to run the script as sudo
def run_full_log_copy_as_sudo():
    #needs a command to cd to whatever directory we save copy_logs.py to
    #something like: 
    #change_directory = "/var//directory/file.py"
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
def parse_log_line(log_line):
    # Define a regular expression pattern to match the log entry format
    log_pattern = r'\[(.*?)\] (\w+)\[(\d+)\] (.+?): (.*)'
    match = re.match(log_pattern, log_line)

    if match:
        timestamp = match.group(1)
        level = match.group(2)
        process_id = match.group(3)
        source = match.group(4)
        message = match.group(5)
        return timestamp, level, process_id, source, message
    else:
        # Return default values or handle the case where the line doesn't match the format
        return None, None, None, None, None



def parse_log_file(log_folder_path):
    log_entries = []

    # List files in the log folder
    log_files = [file for file in os.listdir(log_folder_path) if file.startswith('full-')]
    sorted_log_files = sorted(log_files, key=lambda x: x.split('-')[-1])

    # Use the latest log file
    latest_log_file = sorted_log_files[-1]

    with open(os.path.join(log_folder_path, latest_log_file), 'r') as log_file:
        for line in log_file:
            # Parse the log line and extract relevant information
            timestamp, level, process_id, source, message = parse_log_line(line)

            # Create a dictionary for the log entry
            log_entry = {
                'timestamp': timestamp,
                'level': level,
                'process_id': process_id,
                'source': source,
                'message': message
            }

            log_entries.append(log_entry)

    return log_entries

# Main function
log_folder_path = "/home/mwdevops/json/full"
log_entries = parse_log_file(log_folder_path)

    # Convert the list of log entries to JSON
log_json = json.dumps(log_entries, indent=4)

    # Save the JSON to a file or print it
with open("log_output.json", "w") as json_file:
        json_file.write(log_json)

print(log_entries[0])

#convert each line of JSON to its own file
# List of items you want to make POST requests for
def send_full_logs():
    url = 'https://302d63369ddc4072852f17a5a7b7771e.us-central1.gcp.cloud.es.io:443/search-vocs/_doc?pipeline=ent-search-generic-ingestion'  #depending on how much noise we can filter out it may be easier / make more sense to send data via ingest pipeline over LS
    api_key = 'ZVhUdC1Za0Jack1ZRDc3Q2QwS1E6c0VXZEZ5cEhTNEd1U29YRE11aU53dw=='
    headers = {'Authorization': f'ApiKey {api_key}'}

    items = []
    with open('log_output.json', 'r') as file:
        # Open the JSON file and read its contents
        json_data_list = json.load(file)

        for item in json_data_list:
            response = requests.post(url, headers=headers, json=item)
            if response.status_code == 200:
                print(f"Successfully made POST request for {item}")
            else:
                print(f"Failed to make POST request for {item}. Status code: {response.status_code}")

def log_send_loop():
    global latest_timestamp
    while True:
        run_shell_script()
        run_full_log_copy_as_sudo()
        log_entries = parse_log_file("/home/mwdevops/json/full/")
        convert_freepbx_log()

        # Only send logs since the latest timestamp
        if latest_timestamp:
            filtered_entries = [entry for entry in log_entries if entry['timestamp'] > latest_timestamp]
        else:
            filtered_entries = log_entries

        items = json.dumps(filtered_entries)

        send_full_logs(items)  # Pass the filtered entries to send_full_logs function
        print("full logs")
        # Sleep for a while before checking logs again
        time.sleep(600)  # Sleep for 10 minutes

log_send_loop()