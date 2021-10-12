password = str(input("Enter password: "))

if len(password) < 11:
	print("Password is too short")
else:
	print("Password is a good length")

'''	
if "*" in list(password): #if ["*"] in list(password):
	print("Yes")
else:
	print("No")
'''