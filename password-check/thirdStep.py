password = str(input("Enter password: "))
words = ["password", "123456", "qwerty"]

x = 0

# Does not contain list()

# Check Length from firstStep.py
if len(password) < 11:
	print("Your password is too short")
else:
	# From secondStep.py
	for item in words:
		# From firstStep.py
		if item in password:
			print("Your password may be easy to guess")
			break

		else:
			# Loop from secondStep.py
			x += 1
			if x >= len(words):
				print("Your password is not likely to be guessed")
				break
			else:
				pass
