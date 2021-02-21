'''
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
'''
# https://pythonprinciples.com/challenges/All-equal/

def all_equal(aList):
  index = 0
  index_plus = 0
  max_index = (len(aList) - 1)
  while index <= max_index:
    index_plus = index+1
    if aList[index] == aList[index_plus]:
      if index == (max_index - 1):
        print("All items are equal")
        exit()
    else:
      print("Not all items are equal")
      exit()
    index += 1

all_equal([2,2,2,2])