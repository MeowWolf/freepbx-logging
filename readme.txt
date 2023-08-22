This script is fully written in Python 

Step 1: Run asterisk_logging.py as a start up script

Step 2: asterisk_logging.py calls run_log_copy.py

Step 3: This runs a sudo command to call the copy_logs.py and run it as sudo to move a file from a restricted directory to one that can be written to

Step 4: log_send_loop.py is run which takes the logs from the file in the above step, converts it to JSON format, filters out unnecessary data, then sends that data to the dallas logstash server, which then pipes the data to elastic-search search-vocs index, then it can be visualized in kibana

