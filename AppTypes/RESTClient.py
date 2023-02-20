import requests
import logging


# configure the root logger to write to a file and console
logging.basicConfig(filename='error.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
logging.getLogger().addHandler(console)

# Specify the URL of the REST API endpoint
url = "http://reqres.incom/api/users/2"
logging.info('The URL we are accessing is ' + url)

# Define any query parameters you need to send along with the request
#params = {"param1": "value1", "param2": "value2"}

# Set any request headers if needed (e.g. for authorization)
#headers = {"Content-Type": "Bearer <access_token>"}

try:
# Send the request and store the response in a variable
  response = requests.get(url) #, params=params, headers=headers)
  # Check if the response was successful (i.e. HTTP status code is 200)
  if response.status_code == 200:
    # If successful, retrieve the data from the response
    data = response.json()
    logging.info('The user details were successfully retrieved')
    # Do something with the data (e.g. print it out)
    print(data["data"]["email"])
  else:
    # If unsuccessful, print an error message
    print("Error retrieving data: ", response.status_code, response.reason)
    logging.warning('The user details were NOT successfully retrieved. Error code: ' + response.status_code)

except Exception as ex:
    print(f"We are unable to access the API.")
    logging.error(f'The API request failed. Error Details:', exc_info=True)
    logging.exception(exc_info=True)

