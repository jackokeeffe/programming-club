# Given multiple words as input, give the acronym
# Input: This is an acronym
# Output: T.I.A.A.

charList = list(input("Enter some words: "))

# .upper() turns given string to uppercase
myString = charList[0].upper()

while " " in charList:
	index = charList.index(" ") + 1
	myString += "."
	myString += charList[index].upper()
	charList.pop(charList.index(" "))

# Adds "." after final letter
myString += "."
print(myString)