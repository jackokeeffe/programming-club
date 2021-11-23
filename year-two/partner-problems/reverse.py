'''
**1. Reversed Messages:
- You will be given two lists filled with words.
- Check if the words in the second list are the reversed versions of the words in the first list.
- Make sure to check through every item in the list!
- A template list can be found in the reverseTemplate.py file, feel free to change the words in the list.
'''

# These lists are from the template file
firstWords = ["olleH", "magrorp", "bulc", "nohtyp"]
secondWords = ["Hello", "program", "club", "pytohn"]

# For each item in the secondWords list (start with the first item)
for x in secondWords:
        # Check if the item (x) matches the same index in the firstWords list
        # .index() return the index of the item within the list
        # [::-1] reverses the word (again) to see if it matches with the x word
        # .lower is used to account for differences in capitalization
	if x.lower() == firstWords[secondWords.index(x)][::-1].lower():
		print("These words are reversed")
	else:
		print("These words are not reversed")
