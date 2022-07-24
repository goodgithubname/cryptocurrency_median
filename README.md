# Band Protocol's Take Home Assignment Attempt

## About the package
Includes a function coin_price() which accepts inputs of symbols (list[str]) and returns the median of the price of the included symbols (float).
If a symbol does not have at least three data from the five sources, the function prints out which symbol had insufficient data and returns a NULL instead of the median.

##Getting Prices
All five APIs can provide values of cryptocurrencies in USD assuming the symbols are correct and they exist in the API's market.
CoinMarketCap, Kraken, and OKX are able to give the USD conversion directly by inputting the symbol.

Binance API, however, does not offer any of their cryptocurrency values in USD, but instead USD stablecoins.
To get the price of currencies in USD, I needed to find a way to convert a USD stablecoin back to USD.
Binance US is a sister company of Binance, in which their API offers prices in USD, however, their market is not as big as Binance.
So I fetch the prices in USDT from Binance and get USDT/USD rates from Binance US. From then I can convert the prices from Binance to USD (currency -> USDT -> USD).

GeckoCoin allows for fetching prices in USD however their API only has price tickers for "id"s ("bitcoin","ethereum","tether", etc.).
To get prices, I needed to somehow convert the symbols from the input list to their respective GeckoCoin id.
To do this, I fetched a list of all available tokens in GeckoCoin from their API to search for ids that have the same symbols as the input.
The ids are then used to get prices in USD for the symbols in the list.

##Calculations
The method for finding outliers is to use the lower and upper bounds from calculating the interquartile range because it is a reliable and simple way to find outliers.
Prices that are lower than the lower bound or higher than the upper bound are not included in further calculations.

The valid prices are then used to calculate the average price of a symbol.

Once I have gotten all the average prices for all the symbols in the list, the list of prices is then inputted into a median() from the module statistics to get the median.
A sorted list of prices is also printed for the user to see where the median came from.

##API rates
To not go over the API rate limit, I have added time.sleep() in the function and in between iterations of test cases to ensure that the package is not requesting the API too fast.

##What could be improved
Most of Python's included functions are synchronous, so when the code tries to get prices from an API, it has to wait until it gets that data. 
That waiting time could be used to calculate other things had I made the code asynchronous which would make the code run significantly faster.

And instead of using time.sleep() to delay/prevent hitting the API rate limit, a dedicated function to halt codes when nearing the rate limit might be more efficient.

Making the package more complete, better structured and able to pip install the package

##UPDATE (25/07/2022)
- Implemented asyncio into code to make API calls asynchronous
- Used black formatter to format Python code