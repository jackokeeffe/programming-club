import yfinance as yf

tickers = ['AAPL', 'MSFT', 'TSLA', 'AMD']

keys = ['shortName', 'symbol', 'sector', 'industry', 'website', 'previousClose', 'regularMarketOpen', 'ask']

for x in tickers:
	ticker = yf.Ticker(x)
	for x in keys:
		if x == 'previousClose':
			print('Previous Close: ' + str(ticker.info[x]))
		elif x == "regularMarketOpen":
			print('Regular Market Open: ' + str(ticker.info[x]))
		elif x == "ask":
			print("Current Price: " + str(ticker.info[x]))
			if ticker.info[x] > ticker.info['previousClose']:
				print("Decision: Buy")
			else:
				print("Decision: Sell")
		else:
			print(ticker.info[x])
	print("\n")