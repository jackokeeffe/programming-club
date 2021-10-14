from random import randint, choice

baseNum = randint(1,100)
userNumber = int(input("Guess: "))

def guessNumber():
	if userNumber != baseNum:
		if userNumber > baseNum:
			print("Too High!")
		else:
			print("Too Low!")
	else:
		print("Correct!")

guessNumber()
print("Your number was " + str(baseNum))