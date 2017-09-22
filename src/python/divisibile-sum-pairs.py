#!/bin/python

import sys

def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    for i in range(0, n):
        for j in range (0, i):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)