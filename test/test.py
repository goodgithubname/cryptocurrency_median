from mypackage.calculations.formulas import *
from mypackage.calculations.functions import *

from mypackage.handler.wrapper import *

from testcase import *
import asyncio

import pprint

asyncio.run(coin_price(["BTC", "ETH", "USDT"]))
