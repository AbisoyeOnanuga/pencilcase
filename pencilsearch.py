# Import the requests library
import requests

# Set your subscription key
subscription_key = "your_subscription_key"

# Set your search query
query = "online learning content"

# Set your search parameters
params = {
    "q": query,
    "mkt": "en-US",
    "count": 10,
    "responseFilter": "Webpages"
}

# Set your search endpoint
endpoint = "https://cse.google.com/cse.js?cx=c6456045664d54b97"

# Set your request headers
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key
}

# Make a GET request to the endpoint with the parameters and headers
response = requests.get(endpoint, params=params, headers=headers)

# Parse the response as JSON
data = response.json()

# Print the response status code and data
print(response.status_code)
print(data)
