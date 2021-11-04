import string

# Common passwords which we defined in stepOne.py)
commonPasswords = ["password", "123456", "qwerty"]

password = str(input("Enter password: "))
symbols = string.punctuation

count = 0

# This loop is seperate from the rest of the code, if a macth is found, the rest of the code will not run. If no match is found, it will continue with the rest of the program.

# Most of this code that checks if a password is common is from stepOne.py
for x in commonPasswords:
	# If the password is common, the program will stop
	if x in password:
		print("Match! This password contains the common password: " + x)
		# This will stop the program if the password is common
		exit()
	else:
		pass
	
if len(password) < 12:
	print("Password is too short")
else:
	print("Password is a good length")
	for x in symbols:
		if x in password:
			print("Password contains symbols")
			print("This is a strong password")
			break
		else:
			count +=1
			if count >= len(symbols):
				print("Password does not contain symbols")
			else:
				pass