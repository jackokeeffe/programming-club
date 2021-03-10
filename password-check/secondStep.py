password = str(input("Enter password: "))
symbols = ["*", "!", "&", "%", "$", "#"]
x = 0

if len(password) < 11:
	print("Password is too short")
else:
	print("Password is a good length")
	for items in symbols:
		if list(password).count(items) > 0:
			print("Password contains symbols")
			break
		else:
			x +=1
			if x >= len(symbols):
				print("Password does not contain symbols")
				break
			else:
				pass
