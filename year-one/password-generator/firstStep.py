#2/02/21: Password Generator
#First Step: Create a password that contains only letters
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
sym = '!@#$%^&*?'

def makePass(length):
	password = str()
	while length > 0:
		length -= 1
		password += random.choice(chars)
	print(password)

makePass(20)