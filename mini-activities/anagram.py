# Reference: https://david.elbe.me/developers/hiring/2014/09/17/fizzbuzz-alternatives.html

word = input("Enter word: ")
word_two = input("Enter second word: ")

if len(word) == len(word_two):
  word = list(word)
  word_two = list(word_two)
  count = 0
  for x in word_two:
    letter = word[count]
    if letter in word_two:
      count+=1
      if count == len(word_two):
        print("These strings are anagrams!")
    else:
      print("These strings are not anagrams!")
      break
else:
  print("These strings are not anagrams!")

# Shorter solution using sorted()
# https://www.w3schools.com/python/ref_func_sorted.asp
'''
if sorted(word) == sorted(word_two):
  print("These strings are anagrams!")
else:
  print("These strings are not anagrams!")
'''