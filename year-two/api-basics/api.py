# Libraries used to create API
from flask import Flask
from flask_cors import CORS

# __name__ tells flask where the app is located
app = Flask(__name__)
# Used for a web standard, sometimes, requesting from an API will not work without the CORS Policy.
cors = CORS(app)

# Path to access data (through GET request) - link + /path/
@app.route('/template/')

# Defaults to the top function. This is automatically returned via a GET request.
def data():
	print("Request Received")
	return "OK", 200

app.run()