from flask import Flask, request
# pip install flask-cors
from flask_cors import CORS
import json

# Creating Flask Object
app = Flask(__name__)
cors = CORS(app)

@app.route('/request/', methods=['POST', 'GET'])

def receive():
	# If the request received is a POST...
	if request.method == "POST":
		userData = json.loads(request.data)
		print(userData)
		return "Received", 200

	# If the request received is a GET...
	elif request.method == "GET":
		return "GET request", 200
	else:
		return "Only GET + POST requests are supported", 500

app.run()