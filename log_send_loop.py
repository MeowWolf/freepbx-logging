def log_send_loop():
    global latest_timestamp

     while True:
        run_full_log_copy_as_sudo()
        log_entries = parse_log_file("/home/mwdevops/json/full/full")
        convert_freepbx_log()

        # Only send logs since the latest timestamp
        if latest_timestamp:
            filtered_entries = [entry for entry in log_entries if entry['timestamp'] > latest_timestamp]
        else:
            filtered_entries = log_entries

        items = json.dumps(filtered_entries)

        send_full_logs(items)  # Pass the filtered entries to send_full_logs function

        # Sleep for a while before checking logs again
        time.sleep(600)  # Sleep for 10 minutes

log_send_loop()