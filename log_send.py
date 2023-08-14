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

send_full_logs()