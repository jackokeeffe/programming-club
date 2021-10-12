# 02/09/21: Number Game
# Starter Code: https://we.tl/t-3LhP2OMSaJ
# Guess if a random number is is odd or even (computer will tell you if you are correct).
import random

random_number = random.choice(range(1,100))

def check_number():
	user_guess = input("Do you think the number is odd or even? (odd/even): ")

	if (random_number % 2 == 0):
		if user_guess == "even":
			print("Correct")
		else:
			print("Incorrect")
	else:
		if user_guess == "odd":
			print("Correct")
		else:
			print("Incorrect")

check_number()
print("The number was " + str(random_number))