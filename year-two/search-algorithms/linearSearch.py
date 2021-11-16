'''
Linear Search: sequentially check each element of a list until a match is found or the whole list has been searched.
'''

# This is the random library used a few weeks ago
import random
# Generate a random number bewteen 1 and 100
random_number = random.randint(1,100)
# This variable is used as our guess
guess = 1

def linear_search():
	# This allows us to use x within the function, you could also use a paramater
	global guess
	# If the guess is not the same as the random number
	if guess != random_number:
		# Tell the user the number was incorrect
		print("Incorrect Guess: " + str(guess))
		# Increase the guess by one (linear increase)
		guess+=1
		# Try again with new guess
		linear_search()
	else:
		print("Correct Guess: " + str(random_number))

# Remember to call your functions
linear_search()