#!/bin/python

import sys
import os

def  maxDifference(a):
    max_diff = a[1] - a[0]
    min_element = a[0]
    for x in range(1, len(a)):
        if a[x] < min_element:
            min_element = a[x]
        if (a[x] - min_element) > max_diff:
            max_diff = a[x] - min_element
        """for y in range (x+1, len(a)):
            if x < y and a[x] < a[y]:
                diff = a[y]-a[x]
                if diff > max_diff:
                    max_diff = diff"""
    if max_diff <= 0:
        return -1
    else:
        return max_diff
                
f = open(os.environ['OUTPUT_PATH'], 'w')
    

_a_cnt = 0
_a_cnt = int(raw_input())
_a_i=0
_a = []
while _a_i < _a_cnt:
    _a_item = int(raw_input());
    _a.append(_a_item)
    _a_i+=1
    

res = maxDifference(_a)
f.write(str(res) + "\n")

f.close()