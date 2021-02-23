# Binary Search: also known as half-interval search; finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.

# Inspiration: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

import random
random_number = random.choice(range(1,100))
min = 1
max = 100

def binary_search():
	global min, max
	guess = (min + max)//2
	if guess > random_number:
		print("Too High: " + str(guess))
		max = guess
		#print(guess)
		binary_search()
	elif guess < random_number:
		print("Too Low: " + str(guess))
		min = guess
		#print(guess)
		binary_search()
	else:
		print("Correct Number")
		print(guess)

binary_search()
