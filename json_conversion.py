import json
import re

def parse_log_file(log_file_path):
    log_entries = []
    log_file_path = "/home/mwdevops/json/full/full-20230727"
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Parse the log line and extract relevant information
            timestamp, level, message = parse_log_line(line)

            # Create a dictionary for the log entry
            log_entry = {
                'timestamp': timestamp,
                'level': level,
                'process_id': process_id,
                'source': process,
                'message': message
            }

            log_entries.append(log_entry)

    return log_entries



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
        return timestamp, level, message
    else:
        # Return default values or handle the case where the line doesn't match the format
        return None, None, None, None, None

# Main function
'''if __name__ == "__main__":
    log_file_path = "path_to_your_log_file.log"
    log_entries = parse_log_file(log_file_path)

    # Convert the list of log entries to JSON
    log_json = json.dumps(log_entries, indent=4)

    # Save the JSON to a file or print it
    with open("log_output.json", "w") as json_file:
        json_file.write(log_json)'''
log_file_path = "/home/mwdevops/json/full/full-20230727"
log_entries = parse_log_file(log_file_path)
log_json = json.dumps(log_entries, indent=4)
with open("log_output.json", "w") as json_file:
    #json_file.write(log_json)
    print(log_entries[0])#create for each loop go separate out each log make a request call to that