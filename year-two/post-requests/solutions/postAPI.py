from flask import Flask, request
from flask_cors import CORS
import json

# Creating Flask Object
app = Flask(__name__)
cors = CORS(app)

# make sure that you are requesting from you localport + your extension (in this case "/database/")
# The methods list lets us send either a POST (send) or a GET (receive) request
@app.route('/database/', methods=['POST', 'GET'])

def receive():
	print("Request Received")

	# If the request was a POST...
	if request.method == "POST":
		# Decode userData from JSON into a Python dictionary
		userData = json.loads(request.data)

		# Check the userData using the checkUserData function. Parameter sends the userData into the function
		# The function will return True or False (boolean) and will decide if the user entered the proper data.
		if checkUserData(userData) == True:
			print("User data is OK")
			return "User has been registered", 200
		else:
			print("User data is NOT OK")
			return "Error in user data", 500

	# If the request was a GET...
	elif request.method == "GET":
		# Give the user a template of how they should send the data
		return "POST Template: {'username': username, 'email': email, 'password': password, 'userID': userID}", 200
	else:
		# If anything other than a POST or GET request are sent, return an error.
		return 'POST + GET are the only supported methods', 500

# Checking the data provided via the userData parameter.
def checkUserData(userData):
	# This variable is used to keep track of every test the userData passes.
	verifyCount = 0
	# These numbers are used to check the password.
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

	# If the username is more than 6 characters...
	if len(userData['username']) > 6:
		# Increase count by 1. If count is equal to 3 at the end, the userData passes all the tests.
		verifyCount += 1

	if "@" and ".com" in userData['email']:
		verifyCount += 1

	# If at least one number (from the numbers list) is within the password, it is good to use.
	for item in numbers:
		if str(item) in userData['password']:
			verifyCount += 1
			break

	# If the userData has passed every test...
	if verifyCount == 3:
		return True
	else:
		return False

# Start the "app"/API
app.run()