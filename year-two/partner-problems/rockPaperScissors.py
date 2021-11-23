'''
3. Rock Paper Scissors:
- This can be a challenging program so make sure to brainstorm how you want to approach it before starting to code.
- As a challenge, try to keep your code as short as possible! 
- The rules to Rock Paper Scissors can be found in the README.md file.
'''
import random
moves = ['rock', 'paper', 'scissors']

# This could be changed to random.choice(moves) to select a word instead of a index
computer = random.randint(0, 2)
player = input("Player Move: ")
# Find the index of the player's move in our moves list
playerMove = moves.index(player.lower())

# Let the player know the moves played
# \n creates a new line in our shell
print("\nPlayer plays " + moves[playerMove])
print("Computer plays " + moves[computer])

# If both move indexes are the same, both the player and the computer chose the same move, it's a tie
if playerMove == computer:
	print("It's a tie!")
# This is our long comparison statement, in each of the brakcets are a condition for the computer to win, if any of these are True, the computer wins and the program ends
# Seperating the bracket conditons are or statements. Meaning only one of these values must be true for the computer to win.
# Remeber the numbers represent items within the moves list: moves[0] - 'rock'
elif (playerMove == 0 and computer == 1) or (computer == 0 and playerMove == 2) or (computer == 2 and playerMove == 1):
	print("Computer wins!")
# If the game was not a tie and the computer did not win, the player wins!
else:
	print("Player wins!")
