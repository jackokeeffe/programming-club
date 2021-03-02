def user_save():
	user = input("Input: ")
	if user[0:4] == "save":
		file = open("save.txt", "a")
		file.write(" " + user.split(" ")[1])
	elif user[0:4] == "read":
		file = open("save.txt", "r")
		#.lstrip() removes space at start of .txt file
		print(file.read().lstrip())
	else:
		print("Wrong Command")
user_save()