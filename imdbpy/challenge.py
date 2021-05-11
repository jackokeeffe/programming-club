import imdb

i = imdb.IMDb()

movie_name = input("Enter the name of a film: ")
search_terms = input("Enter terms: ")

searchlist = i.search_movie(movie_name)
id = searchlist[0].movieID
movie = i.get_movie(id)

split_terms = search_terms.split()

for x in split_terms:
	print(movie[x])

'''
Print Director Name (without extra information):
print(str(movie['director']).split("_")[1].split("_"[0])[0])
'''