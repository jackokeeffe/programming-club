# Binary Search: splits the list in half and tries to find the value

import random
# Make sure your number isn't below 1 or above 100
random_number = random.randint(1,100)
# These variables are not within the function as if they were, everytime the function was called (again), the value would set back to 1 & 100
min = 1
max = 100

def binary_search():
	# Allows us to use the variables without resetting the value
	global min, max
	# Choose the middle number between the list
	guess = (min + max)//2
	
	# If the guess is too high...
	if guess > random_number:
		print("Too High: " + str(guess))
		# Set the max to the guess as the number must be smaller
		max = guess
		#print(guess)
		# Try again with new max
		binary_search()

	# If the guess is too low...
	elif guess < random_number:
		print("Too Low: " + str(guess))
		# The number must be > guess, therefore set the minimum value to check to the guess
		min = guess
		#print(guess)
		# Try again with new min
		binary_search()
	else:
		# We can print guess as the number as it now matches
		print("Yay, the algorithm found the number " + str(guess))

# Only printed once, before the function starts
print("Searching for number " + str(random_number))
binary_search()
