import random
import string

chars = string.ascii_lowercase + string.digits

def makePass():
	# int to turn string input into a number
	length = int(input("How long would you like your password: "))
	password = str()
	while length > 0:
		length -= 1
		password += random.choice(chars)
		print(password)
	print(password)

makePass()

# Notes: not guaranteed to include a number
