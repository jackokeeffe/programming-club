'''
2. Multiple List:

- A list and a number (int) should be given as a paramater.
- Make a new list and add any value from the old list that is a multiple of the given number (parameter) to the list.
- Print a statment that shows both the old list and the new list.
'''

# Try removing the multiples of three in this list and see what happens
inputList = [1, 2, 3, 4, 5, 6]
inputMultiple = 3

# Note the parameters, these are in the function call at the bottom
def searchList(myList, multiple):
	# Create a new empty list
	multiplesList = []
	for x in myList:
		# If the element in inputList/multiple has no remainder, it must be a multiple
		if x % multiple == 0:
			# Since this element is a multiple, add it to the new list containing only multiples
			multiplesList.append(x)
			print(str(x) + " is a multiple of " + str(multiple) + " and has been added to the list")
		else:
			print(str(x) + " is not a multiple")

	# (almost) Everything under this comment is optional to add: just some more cool features. 
	# Make sure you print the list for the user so they can see your function work!
	word_count = 0
	# This loop counts the words within the new multiple list
	for x in multiplesList:
		word_count+=1
	# If there are no multiples in the new list...
	if word_count == 0:
		# When you are combining numbers and lists with strings, make sure you turn them to strings using str()
		print("There were no numbers that were a multiple of " + str(multiple) + " in " + str(myList))
	else:
		print("There were " + str(word_count) + " words that were multiples of " + str(multiple) + ". Here is the new list: " + str(multiplesList))

# The parameters refer to the variables above
searchList(inputList, inputMultiple)