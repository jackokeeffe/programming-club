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

# This function will generate a password without symbols, called if symbolsQuestion == "n"
def withoutSym():
	global userLength, password
	while userLength >=0:
		userLength -= 1
		password += random.choice(chars)
	print(password)

# This function will generate a password with symbols, called if symbolsQuestion == "y"
def withSym():
	global password
	# This gives half the length of the password
	floorDiv = userLength // 2
	halfLength = userLength - floorDiv
	while halfLength > 0:
		password += random.choice(chars)
		halfLength -= 1
	# This turns half of the password into symbols, guarantees a symbol within the password.
	# A second approach to this problem can be found in thirdStep-new.py
	while floorDiv > 0:
		password += random.choice(sym)
		# This adds each character one at a time
		floorDiv -= 1
	print(password)

start()