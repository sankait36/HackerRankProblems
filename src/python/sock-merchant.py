#!/bin/python

import sys

def sockMerchant(n, ar):
    # Complete this function
    sock_dict = {}
    for val in ar:
        if val not in sock_dict:
            sock_dict[val] = 0
        sock_dict[val] += 1

    pairs = 0
    for key in sock_dict:
        if sock_dict[key] % 2 == 0:
            pairs += (sock_dict[key]/2)
        elif sock_dict[key] > 2 and sock_dict[key] % 2 != 0:
            to_add = sock_dict[key]/2
            pairs += to_add
    return pairs

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = sockMerchant(n, ar)
print(result)
