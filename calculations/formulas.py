import statistics
import math

from mypackage.handler.wrapper import *


def percentile(data, percent):
    n = len(data)
    p = n * percent / 100
    if p.is_integer():
        return data[int(p)]
    else:
        return data[int(math.ceil(p)) - 1]


def remove_outlier(price_list):
    # Sort price list
    price_list.sort(key=lambda x: x[1])

    prices = []
    for price in price_list:
        prices.append(float(price[1]))

    # Calculate IQR to find lower bound and upper bound
    q25 = percentile(prices, 25)
    q75 = percentile(prices, 75)
    iqr = q75 - q25

    # Calculataing upper/lower bounds
    max = q75 + (1.5 * iqr)
    min = q25 - (1.5 * iqr)

    new_price = []
    # Append to new list if fit in lower/upper bounds
    for markets in price_list:
        if markets[1] > min and markets[1] < max:
            new_price.append(markets[1])
        else:
            print(f"Price from {markets[0]} is an outlier")
    return new_price
