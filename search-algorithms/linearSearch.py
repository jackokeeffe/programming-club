# Linear Search: sequentially check each element of a list until a match is found or the whole list has been searched.

# "We know that linear search on an array of n elements might have to make as many as n guesses." - Khan Academy

import random
random_number = random.choice(range(1,100))
x = 1
def linear_search():
	global x
	guess = x
	if guess != random_number:
		print("Incorrect Guess: " + str(guess))
		x+=1
		linear_search()
	else:
		print("Correct Guess: " + str(random_number))

linear_search()