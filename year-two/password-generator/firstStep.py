import random
import string

# Define a string of chars and numbers.
# A random letter from this strings will be chosen to be added to the password
chars = string.ascii_lowercase + string.digits

# Create a function that takes a number - to be used as the length of the password
def makePass(length):
	# Define an empty string which will be filled char by char to create the password
	password = str()

	# While the length given...
	while length > 0:
		# Subtract 1 from length since we will add one character to password
		length -= 1
		# Add a random letter from chars to the password string
		password += random.choice(chars)
		print(password) # Only used to visualize how the password is formed
	print(password)

# Loop will repeat 20 times/password will be 20 chars long
makePass(20)

# Notes: not guaranteed to include a number