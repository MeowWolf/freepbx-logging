import requests

def send_full_logs():
    items = []
    with open('log_output.json', 'r') as file:
        for line in file:
            items.append(line.strip())

# URL where you want to make the POST requests
    url = 'https://302d63369ddc4072852f17a5a7b7771e.us-central1.gcp.cloud.es.io:443/search-vocs/_doc?pipeline=ent-search-generic-ingestion'  #depending on how much noise we can filter out it may be easier / make more sense to send data via ingest pipeline over LS

# Iterate through the items and make POST requests
    for item in items:
        data = {'item': item}  # You can adjust the payload data as needed
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(f"Successfully made POST request for {item}")
        else:
            print(f"Failed to make POST request for {item}. Status code: {response.status_code}")

send_full_logs()