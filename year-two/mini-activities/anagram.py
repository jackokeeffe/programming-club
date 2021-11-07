'''
3. Anagram:

- Let the user input two words via the console/shell.
- Compare both the strings and check if they are anagrams.
- Let the user know if the inputted words were anagrams.

Note:
- This does not have to work with sentences (spaces and/or punctuation)
'''

word = input("Enter word: ")
word_two = input("Enter second word: ")
# Anagrams must both have the same length, if they don't end the program (not anagrams)
if len(word) == len(word_two):
	# Turn both words into lists (refer to lengthOfNumber)
  word = list(word)
  word_two = list(word_two)
  count = 0
	# This targets letter by letter in second word
  for x in word_two:
		# Target a letter in the first word (follows increasing count variable)
    letter = word[count]
		# If both the letters match, increase count
    if letter in word_two:
      count+=1
			# If count has been increased to the length of the string, every letter must match
      if count == len(word_two):
        print("These strings are anagrams!")
		# If the letter is not in the string, they are not anagrams; end the program
    else:
      print("These strings are not anagrams!")
      break
# If strings are not the same length...
else:
  print("These strings are not anagrams!")

# Shorter solution using sorted()
# https://www.w3schools.com/python/ref_func_sorted.asp
'''
# Sorted turns the words into a list and than sorts the list alphabetically, therefore if the words are anagrams, the sorted lists must be exactly the same
if sorted(word) == sorted(word_two):
  print("These strings are anagrams!")
else:
  print("These strings are not anagrams!")
'''