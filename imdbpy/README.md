### Setup
**Installation**
```
pip install git+https://github.com/alberanid/imdbpy
pip install imdbpy
```

**Get Started**
```
import imdb
i = imdb.IMDb()
searchlist = i.search_movie(moviename)
id = searchlist[0].movieID
movie = i.get_movie(id)
```

### Important Keys
['title'], ['plot'], ['year'], ['director'], ['runtime']

```
print(movie['key'])
```

### Challenge
- Take user input for movie title and keys
- Print the info for the movie based on each key


- Example (Input):
- Input1: The Shining
- Input2: Plot, Director, Runtime

### Resources:
- [IMDB](https://www.imdb.com/)
- [IMDBPY Github] (https://github.com/alberanid/imdbpy)
- [IMDBPY Documentation] (https://imdbpy.readthedocs.io/en/latest/)
- [reelSRCH](https://github.com/jackokeeffe/reelSRCH)