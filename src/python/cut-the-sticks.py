#!/bin/python

import sys


def chop(arr, s):
    for x in range(0, len(arr)):
        arr[x] -= s
    arr[:] = (value for value in arr if value != 0)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
while len(arr) != 0:
    print len(arr)
    chop (arr, min(arr))
