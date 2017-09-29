#!/bin/python

import sys

def twoStrings(s1, s2):
    c = []
    
    temp_c1 = []
    for ch in s1:
        if ch not in temp_c1:
            temp_c1.append(ch)
    c.append(temp_c1)

    temp_c2 = []
    for ch in s2:
        if ch not in temp_c2:
            temp_c2.append(ch)
    c.append(temp_c2)

    result = set(c[0]).intersection(*c)
    if len(result) == 0:
        return "NO"
    else:
        return "YES"

q = int(raw_input().strip())
for a0 in xrange(q):
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = twoStrings(s1, s2)
    print(result)

