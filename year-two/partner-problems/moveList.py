'''
2. Move this List:
- Write a function that rotates a list by k elements.
- If k was 3 and your list was [1, 2, 3, 4, 5], your new list will be [4, 5, 1, 2, 3]
Inspiration for this problem comes from: https://bit.ly/3cIGHXW
'''

originalList = [1, 2, 3, 4, 5]
# This is our k value, our program should account for different k values
k = 3
# This is the new list where we will add our values (in their new order)
newList = []

index = k

# For values between k and the end of the list
while index < len(originalList):
        # Add the item from the original list to our new list
	newList.append(originalList[index])
	index +=1
index = 0
# For values from 0 - k
while index < k:
        # Add these values to the new list
        # Since we already added values, these will appear at the end of the list (as if they have rotated)
	newList.append(originalList[index])
	index += 1
print(newList)
