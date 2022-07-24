import asyncio

from mypackage.calculations import *
from mypackage.handler import *

if __name__ == "__main__":
    exchange_prices = asyncio.run(
        functions.get_exchange_prices(["BTC", "ETH", "NOTAREALTOKEN"])
    )
