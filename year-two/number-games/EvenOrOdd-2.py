'''
Challenge: Allow the user to guess if the number is even or odd. Tell them if they are correct.

Steps:
1. User enters the number
2. Another user can enter a guess, "even" or "odd"
3. Check if they number is even or odd, than check the user's guess to see if they are correct
'''

# Takes user input as an integer
guessThis = int(input("Enter a number: "))
userGuess = str(input("Even or odd: "))

def checkIfEven():
	if userGuess.lower() == "even" and guessThis % 2 == 0:
			print("Correct")
	elif userGuess.lower() == "odd" and guessThis % 2 != 0:
		print("Correct")
	else: 
		print("Incorrect, the number was " + str(guessThis))

checkIfEven()