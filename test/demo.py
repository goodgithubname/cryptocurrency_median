# python libraries
import time

# modules
from mypackage.calculations import *
from mypackage.handler.wrapper import *

# test cases
from testcase import *


for i in range(0, len(test_cases) - 1):
    print(f"TEST CASE: {i+1}")
    print("===============================")
    print(coin_price(test_cases[i]))
    print(f"\n===============================\n")
    time.sleep(3)
