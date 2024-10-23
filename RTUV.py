import urllib.request, json, csv
from datetime import datetime

# OpenUV API URL
url = "https://api.openuv.io/api/v1/uv?lat=29.6516&lng=-82.3248&alt=50"

# API headers (for authorization)
headers = {
    'x-access-token': 'openuv-b2n6tyrm2m1woza-io'  # Replace with your actual API key
}

# Create a request object to fetch data from the OpenUV API
req = urllib.request.Request(url, headers=headers)

# Fetch and read the data from the API
with urllib.request.urlopen(req) as response:
    data = response.read().decode()  # Decode byte data to a string

# Parse the JSON data
uv_data = json.loads(data)

# Extract useful information from the API response
uv_index = uv_data['result']['uv']
uv_max = uv_data['result']['uv_max']
uv_time = uv_data['result']['uv_time']

# Print the extracted UV information
print(f"Current UV Index: {uv_index}")
print(f"Maximum UV Index Today: {uv_max}")
print(f"UV Data Timestamp: {uv_time}")

# Saving the data to a JSON file (similar to downloading a binary file)
with open('uv_data.json', 'w') as json_file:
    json.dump(uv_data, json_file, indent=4)
    print("UV data saved to uv_data.json")

# Log the data to a CSV file
with open('uv_data_log.csv', mode='a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Log the current timestamp, UV index, and maximum UV index
    writer.writerow([datetime.now(), uv_index, uv_max])
    print("UV data logged to uv_data_log.csv")

