# Checking to see if given number, and all of the numbers before it (1-15) is in the prime number list.
# Why is this a bad idea?
# Fix as many of the problems in the code below

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

number = input("Enter a number: ")

length = len(prime_numbers)

while length > 0:
	for prime_numbers in prime_numbers:
		if number.equalTo(prime_numbers):
			print("Prime");
		else:
			print("Not prime");
		length -= 1;