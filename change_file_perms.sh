#!/bin/bash

# Specify the directory to monitor
monitor_dir="/home/mwdevops/json/full/"

# Start inotifywait to monitor the directory for close_write events
inotifywait -m -e close_write --format "%w%f" "$monitor_dir" |
while read -r file_path; do
    chmod +w "$file_path"
    echo "Changed permissions of $file_path to writable."
done
