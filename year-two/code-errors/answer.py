'''
User enters a number bewteen 2 and 97, check if that number is a prime number within the prime_numbers list
Find, identify, and correct as many errors within this program as you can
Don't run the program unless you are stuck!
Hint: There are ~10 errors!

There are many more improvements you could make to this code (stop the program if x > number, and no match was found (this will limit the number of loops within the program)).
Feel free to add any changes and message them to me, I will add them to the Github solution.
'''

def checkPrime(number, prime_numbers):
	matchCount = 0
	for x in prime_numbers:
		if number == x:
			print(str(number) + " is prime");
			# Even if we were told the number was prime, the program would still check other items in this list. 
			# Break ends the loop after this is printed
			break
		else:
			print(str(x) + " does not match with our number");
			# Increase each time there is no match
			matchCount +=1
			# If we have not matched for every element in the list, we know the number cannot be prime
			if matchCount == len(prime_numbers):
				print(str(number) + " is not prime!")
			# This else statement is not needed but it can help to visualize what the code is doing.
			else:
				# "pass" does nothing, it just continues with the program as if nothing happened
				pass

# This is where the program starts running
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

number = int(input("Enter a number: "))

if number <= 97 and number >= 2:
	# This number is okay to use (within 2-97")
	# Calls the function at the top of this file
	checkPrime(number, prime_numbers)
else:
	# This number cannot be used, not within the range of prime_numbers
	print("Enter a number between 2 and 97")
