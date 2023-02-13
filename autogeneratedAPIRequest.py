import requests
import json

# Replace YOUR_DATABRICKS_DOMAIN with the URL of your Databricks instance (e.g. https://eastus.azuredatabricks.net)
DATABRICKS_DOMAIN = "https://adb-5595195760454296.16.azuredatabricks.net"

# Replace YOUR_API_KEY with your Databricks API key
API_KEY = "dapif04aab29bb41fcfb0b00480e0e679c07"

# Replace YOUR_CLUSTER_ID with the ID of your Databricks cluster
CLUSTER_ID = "0201-101611-o3q4m3vr"

# Define the Spark SQL query you want to execute
QUERY = "SELECT * FROM hive_metastore.default.diamonds"

# Set up the headers for the HTTP request
HEADERS = {
    "Authorization": "Bearer " + API_KEY,
    "Content-Type": "application/json"
}

# Set up the URL for the query endpoint
QUERY_URL = DATABRICKS_DOMAIN + "/api/2.0/preview/sql/queries"

# Set up the JSON payload for the HTTP request
PAYLOAD = {
    "cluster_id": CLUSTER_ID,
    "command": QUERY
}

# Execute the query and store the response
response = requests.post(QUERY_URL, headers=HEADERS, data=json.dumps(PAYLOAD))

# If the query was successful, print the results
if response.status_code == 200:
    print(response.json()["rows"])
else:
    print("Query failed with status code " + str(response.status_code))
