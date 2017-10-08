# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import floor
def binary_search(l, r, arr, val):
    mid = int(floor((l+r)/2))
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return binary_search(0, mid, arr, val)
    else:
        return binary_search(mid+1, len(arr)-1, arr, val)


v = int(raw_input().strip())
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
res = binary_search(0, len(arr)-1, arr, v)
print res