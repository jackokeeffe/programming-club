# Takes user input as an integer
userNumber = int(input("Enter a number: "))

def checkIfEven():
	# Checks if number/2 has no remainder - even, or # = 1
	if userNumber % 2 == 0:
		print("Number entered is even")
	else: # If it's not even, it must be odd
		print("Number entered is odd")

checkIfEven()