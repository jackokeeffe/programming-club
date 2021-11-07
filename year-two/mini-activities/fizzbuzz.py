'''
1. FizzBuzz:
- Write a program that prints the numbers from 1 to 100.
- For multiples of three print “Fizz” instead of the number.
- For the multiples of five print “Buzz”.
- For numbers which are multiples of both three and five print “FizzBuzz”.
'''

# This is not 0 as we want to print from 1-100
x = 1
while x < 100:
	# If x/3 and x/5 leave no remainder...
	# Note that this is checked before any other multiple 
  if x % 3 == 0 and x % 5 == 0:
		# It must be a multiple of both, therefore print 'FizzBuzz'
    print("FizzBuzz")
  else:
		# If only a multiple of three...
    if x % 3 == 0:
      print("Fizz")
		# If only a multiple of five...
    elif x % 5 == 0:
      print("Buzz")
		# If it is not a multiple of 3 or 5, just print x (the number between 1-100)
    else:
      print(x)
	# Add one to x until it equals 100, than the loop will stop
  x += 1