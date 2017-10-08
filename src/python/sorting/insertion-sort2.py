#!/bin/python
def insertionSort(ar):
    for y in range(1, len(ar)):    
        val_to_insert = ar[y]
        i = y-1

        while i >= 0 and val_to_insert < ar[i]:
            ar[i+1] = ar[i]
            i -= 1

        ar[i+1] = val_to_insert
        sarr = [str(a) for a in ar]
        print ' '.join(sarr)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)