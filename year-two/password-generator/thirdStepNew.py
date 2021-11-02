'''
The original program for this challenge included floor division, which ensured half of the password would be composed of symbols.
Due to Mr. Bush's suggestion, I have changed this to make a new password if the program did not randomly add a symbol in the password.
Due to this change there is a (very) small chance that this program could never select a symbol and run infinitely.

A link to the original solution will be in README.md (but it is a little more complicated than this solution).
'''

import random
import string

# Our password will be made out of these randomly selected characters (and maybe some symbols)
chars = string.ascii_lowercase + string.digits
	
# This function will create the password
def generatePassword():
	# global, allows us to use these variables in checkPassword
	global chars, password, symbolQuestion
	# Define the password as a blank string waiting to be created
	password = str()

	length = int(input("How long would you like your password: "))
	symbolQuestion = input("Would you like symbols in your password (y/n): ")

	# If the user wants symbols...
	if symbolQuestion.lower() == "y":
		# Add symbols to the character list that will make up the password
		chars += string.punctuation

	# If they did not want symbols ("n"), the list will remain untouched

	# This will generate the password to the user's desired length
	while(length > 0):
		# Add one character from the list
		password += random.choice(chars)
		length -=1

	# Calling our checkPassword function to check the given parameter, our created password
	checkPassword(password)


# This is created as a there is a small chance that even if the user requested symbols, the program may have randomly selected characters that were not symbols
def checkPassword(password):
	count = 0

	# If the user wanted symbols...
	if symbolQuestion.lower() == "y":
		# Iterate through each character in the string
		for x in string.punctuation:
			# Check if the character is in the password
			if x in password:
				# If there happens to be one symbol, its a good password!
				print(password)
				break
			# If the symbol is not in the password...
			else:
				# Check to see if every symbol has been checked
				if count == len(string.punctuation):
					# If this is true, there are no symbols in the password. Therefore, we will try and generate a new password
					generatePassword()
				else:
					# If there was not a symbol in the password but the program has not checked every symbol, increase the count by one and try again
					count +=1 
	# If they did not want symbols just give them the password
	else:
		print(password)

generatePassword()
