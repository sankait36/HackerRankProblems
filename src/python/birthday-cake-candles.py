#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_height = max(ar)
    tallest_candle_count = 0
    for val in ar:
        if val == max_height:
            tallest_candle_count += 1
    return tallest_candle_count

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
