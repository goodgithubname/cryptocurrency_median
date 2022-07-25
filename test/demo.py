# python libraries
import asyncio
import json

# modules
from mypackage.calculations.functions import *
from mypackage.handler import *

# load test_cases.json
with open("test_cases.json", "r") as j:
    data = json.load(j)


if __name__ == "__main__":
    for i in data:
        print(f"TEST CASE: {i}")
        print("===============================")
        print(asyncio.run(get_exchange_prices(data[i])))
        print(f"\n===============================\n")
