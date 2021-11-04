# This program will see if these letters are in a string
myList = ['r', 's', 'g', 'c']
schoolName = "Royal St. George's College"

# Iterate through each letter in the list
for x in myList:
	#.lower() because 'c' doesn't match 'C'
	if x in schoolName.lower():
		print("Match! This string contains the letter " + x + "!")
	else:
		print("Not a match! This string does not contain the letter " + x + "!")