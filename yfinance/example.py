#pip install yfinance
import yfinance as yf

ticker = yf.Ticker("TSLA")

'''
Some Popular Stocks:
MSFT
AAPL
TSLA
AMD
NVDA
'''

# See all information
print(ticker.info['sector'])

# Target the 'ask' key in dictionary
print(ticker.info['ask'])

'''
Interesting Keys:
- 'sector':
-	'website'
-	'industry'
-	'previousClose'
-	'regularMarketOpen'
-	'shortName'
-	'symbol'
'''

keys = ['shortName', 'symbol', 'sector', 'industry', 'website', 'previousClose', 'regularMarketOpen']

for x in keys:
	print(ticker.info[x])

# Other Interesting Functions:

print(ticker.financials)

print(ticker.recommendations)

print(ticker.history(period="max"))