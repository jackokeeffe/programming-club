word = "apple"
turns = 3

def hangman():
	global turns
	print("Hint: It is a fruit and has 5 letters.")
	guess = input("Guess the word: ")
	# .lower() lowers the user's guess so capitalized guesses will be properly checked.
	guess = guess.lower()
	if guess != word:
		turns -= 1
		if turns > 0:
			print(str(turns) + " guesses left")
			hangman()
		elif turns <= 0:
			print("Game Over")
	elif guess == word:
		print("Correct word")

hangman()