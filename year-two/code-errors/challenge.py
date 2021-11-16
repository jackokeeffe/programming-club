'''
User enters a number bewteen 2 and 97, check if that number is a prime number within the prime_numbers list
Find, identify, and correct as many errors within this program as you can!
Don't run the program unless you are stuck!
Hint: There are ~7 errors!
'''

def checkPrime(length, prime_numbers):
	while length < 0:
		for prime_numbers in prime_numbers:
			if number.equalTo(prime_numbers):
				print(number + " is prime");
			else:
				print(number + " is not prime");
			length += 1;

# This is where the program starts running
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

number = input("Enter a number: ")
length = len(prime_numbers)

if number >= 97 or number < 2:
	# This number is okay to use (within 2-97")
	# Calls the function at the top of this file
	checkPrime(prime_numbers, length)
else:
	# This number cannot be used, not within the range of prime_numbers
	print("Enter a number between 2 and 97")

