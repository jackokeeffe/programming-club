import requests
import json

# Notice that this link contains the extension "/request/"
APILink = "http://127.0.0.1:5000/request/"

def postData():
	postData = {'Name': "Bob", 'School': "RSGC", 'Age': 16.5, 'Grade': 11}
	postDataJSON = json.dumps(postData)
	request = requests.post(APILink, postDataJSON)
	print(request.status_code, request.reason)

def getData():
	request = requests.get(APILink)
	print(request.content)

getData()