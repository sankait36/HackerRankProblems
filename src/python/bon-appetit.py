#!/bin/python

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    anna_cost = 0
    for x in range(0, n):
        if x != k:
            anna_cost += ar[x]
    
    anna_cost = anna_cost/2

    if anna_cost == b:
        return 'Bon Appetit'
    else:
        return str(b-anna_cost)

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
