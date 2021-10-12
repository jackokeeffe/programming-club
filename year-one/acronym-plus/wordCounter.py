# Goes over .index(), list(), .pop(), while loops
# Example: https://wordcounter.net

string = "There is nothing like looking, if you want to find something. You certainly usually find something, if you look, but it is not always quite the something you were after."

word_count = 0
split_list = list(string)
print(split_list)
characters = len(split_list)

while " " in split_list:
	index = split_list.index(" ")
	word_count += 1
	split_list.pop(index)

# +1 fixes one word missed when basing on spaces (misses first word)
print(str(word_count + 1) + " words")
print(str(characters) + " characters")