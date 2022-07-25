from statistics import median
import time
import asyncio

from mypackage.calculations.formulas import *
from mypackage.handler.wrapper import *


def get_gecko_id(symbol, gecko_list):
    for ids in gecko_list:
        if symbol.lower() == ids["symbol"]:
            return ids["id"]
    return None


def get_gecko_id_multiple(symbol, gecko_list):
    id_list = []
    for ids in gecko_list:
        if symbol.lower() == ids["symbol"]:
            id_list.append(ids)
    print(id_list)
    print(len(id_list))
    if len(id_list) > 1:
        print(f"\nMore than 1 currencies for the symbol {symbol} in CoinGecko")
        for dupe in range(1, len(id_list) + 1):
            print(f"[{dupe}]: {id_list[dupe-1]['name']}")
        choice = int(input("Which one would  you like to input?:\n"))
        print(id_list[choice - 1]["id"])
        return id_list[choice - 1]["id"]
    elif len(id_list) == 1:
        print(id_list[0]["id"])
        return id_list[0]["id"]
    else:
        return None


def remove_null(price_list):
    new_price = []
    # Remove price with no data
    for price in price_list:
        if price[1] != None:
            new_price.append(price)
        """else:
            print(f"{price[0]} no data...")"""

    return new_price


# This function creates a 2d array [Currency, avg Price] from multiple APIs and returns median
async def get_exchange_prices(symbol_list):
    # Remove duplicates from list
    symbol_list = list(dict.fromkeys(symbol_list))

    # Get lists of currencies from gecko
    gecko_list = gecko_id_list()

    input_list = []
    print(symbol_list)

    # Iterate all smybols
    for symbol in symbol_list:
        print(f"Calculating for symbol {symbol}")
        median_prices = []
        # Get price from all APIs and put them in a list(except ones without data)
        print("Fetching from Binance")
        binance = asyncio.create_task(binance_price(symbol))

        print("Fetching from GeckoCoin")
        gecko = asyncio.create_task(gecko_price(get_gecko_id(symbol, gecko_list)))

        print("Fetching from CoinMarketCap")
        coinmarket = asyncio.create_task(coinmarketcap_price(symbol))

        print("Fetching from Kraken")
        kraken = asyncio.create_task(kraken_price(symbol))

        print("Fetching from OKX")
        okx = asyncio.create_task(okx_price(symbol))

        # await asyncio functions
        binance_value = await binance
        all_price.append(["Binance", binance_value])
        gecko_value = await binance
        all_price.append(["GeckoCoin", gecko_value])
        coinmarket_value = await coinmarket
        all_price.append(["CoinMarketCap", coinmarket_value])
        kraken_value = await coinmarket
        all_price.append(["Kraken", kraken_value])
        okx_value = await coinmarket
        all_price.append(["OKX", okx_value])

        # Remove null prices and check if 3 or more sources a re provided
        all_price = remove_null(all_price)
        if len(all_price) < 3:
            print(f"Less than 3 sources for symbol {symbol}")
            time.sleep(1)
            return None
        all_price = remove_outlier(all_price)

        # Pair symbol with average price
        median_prices.append(median(all_price))
        print(median_prices)
        time.sleep(1)

    return median_prices
