#!/bin/python

import sys

def gemstones(arr):
    c = []
    for x in range(0, len(arr)):
        temp_c = []
        for ch in arr[x]:
            if ch not in temp_c:
                temp_c.append(ch)
        c.append(temp_c)

    result = set(c[0]).intersection(*c)
    return len(result)

n = int(raw_input().strip())
arr = []
arr_i = 0
for arr_i in xrange(n):
    arr_t = str(raw_input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)