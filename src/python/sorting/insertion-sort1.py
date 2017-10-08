#!/bin/python
def insertionSort(ar):    
    val_to_insert = ar[len(ar)-1]
    i = 0
    while val_to_insert > ar[i]:
        i += 1

    for x in range(len(ar)-1, i, -1):
        ar[x] = ar[x-1]
        sarr = [str(a) for a in ar]
        print ' '.join(sarr)

    ar[i] = val_to_insert
    sarr = [str(a) for a in ar]
    print ' '.join(sarr)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
