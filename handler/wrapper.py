from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import requests
import json

# Get price from Binance
async def binance_price(symbol):
    try:
        binance_url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
        data = requests.get(binance_url)
        data = data.json()

        usdt_price = requests.get(
            "https://api.binance.us/api/v3/ticker/price?symbol=USDTUSD"
        )
        usdt_price = usdt_price.json()

        if symbol == "USDT":
            return float(usdt_price["price"])

        if "code" in data.keys():
            # print(data['msg'])
            return None

        return float(data["price"]) * float(usdt_price["price"])
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Return list of currencies in CoinGecko
def gecko_id_list():
    try:
        gecko_url = "https://api.coingecko.com/api/v3/coins/list"
        data = requests.get(gecko_url)
        data = data.json()
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Get price from CoinGecko
async def gecko_price(id):
    try:
        if id == None:
            print("No data found for CoinGecko")
            return None
        else:
            # Get current price from coin id
            gecko_url = f"https://api.coingecko.com/api/v3/coins/{id}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=true&sparkline=false"
            data = requests.get(gecko_url)
            data = data.json()
            return data["market_data"]["current_price"]["usd"]

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Get price from CoinMarketCap
async def coinmarketcap_price(symbol):
    coinmarketcap_url = (
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    )

    parameters = {"symbol": symbol, "convert": "USD"}
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": "API_KEY",
    }

    session = Session()
    session.headers.update(headers)
    try:
        response = session.get(coinmarketcap_url, params=parameters)
        data = json.loads(response.text)
        # Gets FAIL if symbol not found
        if len(list(data["data"].keys())) == 0:
            # print(f"No data found for CoinMarketCap")
            return None
        else:
            return data["data"][symbol]["quote"]["USD"]["price"]
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


# Fetch price from Kraken
async def kraken_price(symbol):
    kraken_url = f"https://api.kraken.com/0/public/Ticker?pair={symbol}USD"
    data = requests.get(kraken_url)
    data = data.json()
    if not data["error"]:
        dict_name = list(data["result"])[0]
        return float(data["result"][dict_name]["p"][0])
    else:
        # print(data['error'][0])
        return None


async def okx_price(symbol):
    okx_url = f"https://www.okx.com/api/v5/market/ticker?instId={symbol}-USD-SWAP"
    data = requests.get(okx_url)
    data = data.json()
    if data["code"] == "0":
        return float(data["data"][0]["last"])
    else:
        # print(f"Error Code {data['code']}: {data['msg']}")
        return None
