#log_parsing_and_conversion.py
#Parses log entries into a list item called log_entries
import json


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