#Third Step: Create a password that contains letters and symbols
import random

password = str()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
sym = '!@#$%^&*?'

def start():
	global userLength
	userLength = int(input("Length of password: "))

	symbolsQuestion = str(input("Do you want symbols in your password (y/n): "))

	if symbolsQuestion == "y":
		withSym()
	else:
		withoutSym()

def withoutSym():
	global userLength, password
	while userLength >=0:
		userLength -= 1
		password += random.choice(chars)
	print(password)

def withSym():
	global password
	floorDiv = userLength // 2
	halfLength = userLength - floorDiv
	while halfLength > 0:
		password += random.choice(chars)
		halfLength -= 1
	while floorDiv > 0:
		password += random.choice(sym)
		floorDiv -= 1
	print(password)

start()