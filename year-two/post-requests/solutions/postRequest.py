# Using the requests' library, we can request information from an API endpoint
import requests
import json
import random

# Notice that this link contains the extension added in postAPI
APILink = "http://127.0.0.1:5000/database/"

# This method will let the user sign-up and send their info to the API.
def postData():
	# Let user "sign-up" and enter their data.
	username = input("Username: ")
	email = input("Email: ")
	password = input("Password: ")
	# Generate a userID for the user (to store in a potential database)
	userID = random.randint(0, 1000)

	# Format the data into a Python Dictionary
	userData = {'username': username, 'email': email, 'password': password, 'userID': userID}
	# Encode the Python Dictionary into a JSON file (to be sent to the API)
	userDataJSON = json.dumps(userData)

	# Send a POST request to the API (via the link) containing the JSON userData
	request = requests.post(APILink, userDataJSON)

	# Let us know the status code and the reason for the specific status code
	# For more on status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
	print(request.status_code, request.reason)

# If called, this will send a GET request to the API, returning the format for the userData
def getData():
	# Send request to the API (via the link)
	request = requests.get(APILink)
	# Print the response string.
	# "Response is OK", 200 - request.content will print "Response is OK"
	print(request.content)

# Make sure you call the functions in order to run them
getData()