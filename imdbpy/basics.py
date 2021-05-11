import imdb

moviename = input("Enter a movie: ")

i = imdb.IMDb()

searchlist = i.search_movie(moviename)
id = searchlist[0].movieID
movie = i.get_movie(id)

#print(movie)

keys = ['title', 'plot', 'year', 'director', 'runtime']

for x in keys:
	print(movie[x])

print(movie['cast'])
print("First Cast Member: " + movie['cast'][0])