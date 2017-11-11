from math import floor
n = int(raw_input().strip())

received = 5
liked = 2
for x in range(1, n):
    received = floor(received/2) * 3
    liked += floor(received/2)

print int(liked)