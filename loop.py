import requests

# List of items you want to make POST requests for
items = ['item1', 'item2', 'item3']

# URL where you want to make the POST requests
url = 'https://example.com/api/endpoint'

# Iterate through the items and make POST requests
for item in items:
    data = {'item': item}  # You can adjust the payload data as needed
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print(f"Successfully made POST request for {item}")
    else:
        print(f"Failed to make POST request for {item}. Status code: {response.status_code}")