# Remeber this from last Tuesday?
import string

# This is the password the user wants to check
password = str(input("Enter password: "))

# If a password contains at on symbol contained in this, it will pass the second test
symbols = string.punctuation

# This is used to count how many times the password has been checked for symbols
count = 0

# If the password is less than 12 characters, its too short!
if len(password) < 12:
	print("Password is too short")
else:
	# If it is over 11 characters, check if it has symbols
	print("Password is a good length")
	# For each item in the symbols list...
	for x in symbols:
		# Count how many times it is in the password
		if x in password:
			print("Password contains symbols")
			print("This is a strong password")
			break
		else:
			count +=1
			# If every symbol has been checked and no matches have been found, there must be no symbols
			if count >= len(symbols):
				print("Password does not contain symbols")
				break
				# This is not needed but it may make it easier to visualize
			else:
				pass