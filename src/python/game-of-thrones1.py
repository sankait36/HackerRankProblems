#!/bin/python

import sys

def gameOfThrones(s):
    # Complete this function
    alcounts = {}
    for ch in s:
        if ch not in alcounts:
            alcounts[ch] = 0
        alcounts[ch] += 1
    
    s_list = list(s)
    if len(s_list) % 2 == 0:
        for key in alcounts:
            if alcounts[key] % 2 != 0:
                return "NO"
        return "YES"
    else:
        odd_one_seen = False
        for key in alcounts:
            if alcounts[key] % 2 != 0:
                if odd_one_seen:
                    return "NO"
                else:
                    odd_one_seen = True
            else:
                if alcounts[key] % 2 != 0:
                    return "NO" 

        return "YES"

s = raw_input().strip()
result = gameOfThrones(s)
print(result)
