import imdb

moviename = input("Enter a movie: ")
i = imdb.IMDb()
x = 0

def search_title(x):
	global movie
	searchlist = i.search_movie(moviename)
	id = searchlist[x].movieID
	movie = i.get_movie(id)

	print(movie['title'])
	print("Starring " + str(movie['cast'][0]) + " and " + str(movie['cast'][1]))

	correct = input("Is this the correct movie? ")
	if correct.lower() == "yes":
		rating()
	else:
		x += 1
		search_title(x)

def rating():
	stars = input("Rating: ")
	final_rating = movie['title'] + " " + stars + "\n"
	file = open("myratings.txt", "a")
	file.write(final_rating)

search_title(x)
