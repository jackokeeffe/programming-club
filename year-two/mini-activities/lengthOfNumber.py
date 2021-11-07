'''
0. Length of a Number:
- Create a function that takes an integer as a parameter
- Return the length of the parameter number but DO NOT use the len() function.
'''

# 'num' is the parameter, can be used to reference the number in the function call
def length(num):
	# Turn the number into a string
	num = str(num)
	# Turn the string into a list with each letter as a seperate element ex. ['H', 'E', 'L', 'L', 'O']
	myList = list(num)
	# This variable is used to count the characters
	count = 0
	# For each letter in the list add one to count
	for x in myList:
		count += 1
	print(count)

# The 5000 is num (the parameter) and is the number whose length will be evaluated
length(5000)