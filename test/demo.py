# python libraries
import asyncio

# modules
from mypackage.calculations.functions import *
from mypackage.handler import *

# test cases
from testcase import *


for i in range(0, len(test_cases) - 1):
    print(f"TEST CASE: {i+1}")
    print("===============================")
    print(asyncio.run(get_exchange_prices(test_cases[i])))
    print(f"\n===============================\n")
