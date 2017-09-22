#!/bin/python

import sys

def migratoryBirds(n, ar):
    # Complete this function
    bird_counts = {}
    for i in range (0, n):
        if ar[i] not in bird_counts:
            bird_counts[ar[i]] = 0
        bird_counts[ar[i]] += 1

    max_id = 0
    max_count = 0
    for key in bird_counts:
        if bird_counts[key] > max_count:
            max_count = bird_counts[key]
            max_id = key

    return max_id

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)