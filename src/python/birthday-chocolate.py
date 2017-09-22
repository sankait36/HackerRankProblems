#!/bin/python

import sys

def solve(n, s, d, m):
    sum_counts = 0
    for i in range(0, n):
        sum = 0
        for j in range(i, m+i):
            if j >= len(s):
                sum += 0
            else:
                sum += s[j]
        if sum == d:
            sum_counts += 1
    return sum_counts

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
