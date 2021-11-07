'''
4. All Equal

- A list should be given via a parameter.
- Create a function that checks to see if every element in the list is equal 
ex. In the list [1, 1, 1, 1], every element is equal.
'''

def all_equal(numberList):
	index = 0
	index_plus = 0
	# This is the length of the list - 1 (to account for index_plus, one above index)
	max_index = (len(numberList) - 1)
	# <= is less than or equal
	while index <= max_index:
		index_plus = index+1
		# If the selected element in the list is equal to the next element...
		if numberList[index] == numberList[index_plus]:
			# If the whole list has been iterated through...
			if index == (max_index - 1):
				print("All items are equal")
				# This ends the program (similar to break but not just for loops)
				exit()
    # If the numbers did not match, every item cannot be equal
		else:
			print("Not all items are equal")
			exit()
		# Increase index by one and repeat
		index += 1

all_equal([2,2,2,2])