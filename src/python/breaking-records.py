#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    curr_max = s[0]
    curr_min = s[0]
    count_max = 0
    count_min = 0
    for x in range(0, len(s)):
        if s[x] > curr_max:
            curr_max = s[x]
            count_max += 1
        if s[x] < curr_min:
            curr_min = s[x]
            count_min += 1
    return(count_max, count_min)


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
