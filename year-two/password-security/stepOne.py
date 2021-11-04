# Challenge 1: Check to see if a password is "common"
commonPasswords = ["password", "123456", "qwerty"]

password = input("Enter a password: ")
for x in commonPasswords:
	if x in password:
		print("Match! This password contains the common password: " + x)
	else:
		print("Not a match! This password does not contain the common password: " + x)