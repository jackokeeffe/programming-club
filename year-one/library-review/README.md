## Library Review
Since there are many libraries which can take a while to learn (pandas, tensorflow, matplotlib), today lets review the past two libraires we've used (IMDBPY & yfinance).

### pip
"pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes." - [PyPi](https://pypi.org/project/pip/#description)

Installing a library:

`pip install libraryname`

Check if pip is installed:

`python -m pip --version`

### Getting Started:
```
import imdb
i = imdb.IMDb()
searchlist = i.search_movie(moviename)
id = searchlist[0].movieID
movie = i.get_movie(id)
```

```
import yfinance
ticker = yf.Ticker("TSLA")
```

### Challenge:
- Create something that allows a user to view information based off the corresponding (or both) library.

### Examples:
- yfinance: If a stock market price falls below a set price, tell the user to sell (different low per stock).
- IMDBPY: Built a text-based rating system (maybe even save the ratings in a [text document](https://github.com/jackokeeffe/programming-club/tree/master/edit-files))
- Feel free to create anything else that uses these libraries.

### Resources:
- [yfinance Documentation](https://pypi.org/project/yfinance/)
- [IMDBPY Documentation](https://imdbpy.readthedocs.io/en/latest/)
- [yfinance Project (Github)](https://github.com/jackokeeffe/programming-club/tree/master/yfinance)
- [IMDBPY Project (Github)](https://github.com/jackokeeffe/programming-club/tree/master/imdbpy)
- [Github Student Devloper Pack](https://education.github.com/pack)