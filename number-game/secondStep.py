# Combined with the first program, now the computer computer should say if the guessed number
# is correct or too high/low.

import random

random_number = random.choice(range(1,100))
guesses = 10

def check_number():
	user_guess = input("Do you think the number is odd or even? (odd/even): ")

	if (random_number % 2 == 0):
		if user_guess == "even":
			print("Correct")
		else:
			print("Incorrect")

	elif (random_number % 2 != 0):
		if user_guess == "odd":
			print("Correct")
		else:
			print("Incorrect")
	number_guess()

def number_guess():
	global user_number_guess, guesses
	user_number_guess = int(input("What do you think the number is: "))
	if user_number_guess == random_number:
		print("Correct")
	elif user_number_guess != random_number:
		guesses -=1
		incorrect()

def incorrect():
	if user_number_guess > random_number:
		print("Your guess was too high")
	else:
		print("Your guess was too low")
	print('You have ' + str(guesses) + " left")
	number_guess()

check_number()
print("The number was " + str(random_number))