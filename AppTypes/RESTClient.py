import requests

# Specify the URL of the REST API endpoint
url = "https://api.example.com/data"

# Define any query parameters you need to send along with the request
params = {"param1": "value1", "param2": "value2"}

# Set any request headers if needed (e.g. for authorization)
headers = {"Authorization": "Bearer <access_token>"}

# Send the request and store the response in a variable
response = requests.get(url, params=params, headers=headers)

# Check if the response was successful (i.e. HTTP status code is 200)
if response.status_code == 200:
    # If successful, retrieve the data from the response
    data = response.json()
    # Do something with the data (e.g. print it out)
    print(data)
else:
    # If unsuccessful, print an error message
    print("Error retrieving data: ", response.status_code, response.reason)
