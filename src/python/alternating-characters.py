#!/bin/python

import sys

def alternatingCharacters(s):
    # Complete this function
    s_list = list(s)
    counts = 0
    for y in range(1, len(s_list)):
        if s_list[y] == s_list[y-1]:
            counts += 1
    return counts

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = alternatingCharacters(s)
    print(result)
