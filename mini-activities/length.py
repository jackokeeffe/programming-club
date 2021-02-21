# Create a function that takes a number num and returns its length.
# The use of the len() function is prohibited.
# https://edabit.com/challenge/2zKetgAJp4WRFXiDT

def length(num):
  num = str(num)
  myList = list(num)
  count = 0
  for x in myList:
    count += 1
  print(count)

length(5000)