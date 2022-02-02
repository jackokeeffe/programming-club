# Using the requests library, we can request information from an API endpoint
import requests

# Request joke data from the API
def requestData():
	# The URL for this website is very readable
	url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart"
	
	# This uses the GET protocol to "get" jokes from the API
	raw = requests.get(url)
	# Data is returned to us in JSON/Dictionary form
	return raw.json()


dataReturned = requestData()

print(dataReturned['setup'] + " " + dataReturned['delivery'])