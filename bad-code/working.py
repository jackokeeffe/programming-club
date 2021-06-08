# Adapted from: https://bit.ly/3glakQb

number = int(input("Enter a number: "))
x = 1

while x <= number:  # Run program until x is even to number
	if x > 1:  # 1 is not a prime number
		# Range does not start at 1 because everything is divisible by 1
		for y in range(2, x):  # Finding factors
			if (x % y) == 0:  # If divisible, not prime
				print(str(x) + " is not a prime number")
				break
		else:  # Else, it must be prime
			print(str(x) + " is a prime number")

	else:  # If number is not greater than one
		print(str(x) + " is not a prime number")
	x += 1
