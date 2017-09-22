#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))

min_sum = sum(arr) - max(arr)
max_sum = sum(arr) - min(arr)

print "%s %s" % (min_sum, max_sum)