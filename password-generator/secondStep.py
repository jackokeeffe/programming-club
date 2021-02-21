#Second Step: Create a password that contains only letters (with user input)
import random

password = str()

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
sym = '!@#$%^&*?'

userLength = int(input("Length of password: "))

def withoutSym():
	global userLength, password
	while userLength >=0:
		userLength -= 1
		password += random.choice(chars)
	print(password)

withoutSym()