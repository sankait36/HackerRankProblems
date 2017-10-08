#!/bin/python

import sys

"""INITIAL TRY
def getMoneySpent(keyboards, drives, s):
    # Complete this function
    if min(keyboards) > s or min(drives) > s:
        return -1
    total_list = []
    for x in range(0, len(keyboards)):
        for y in range(0, len(drives)):
            price = keyboards[x] + drives[y]
            if price == s:
                # No better combination than spending all the money
                return s
            else:
                total_list.append(price)
                
    if len(total_list) == 0:
        return -1
    else:
        max_price = -1
        for val in total_list:
            if val < s and val > max_price:
                max_price = val
        return max_price
"""

# Reading the discussion a better way would be to sort the keyboards in descencing 
# and drives in ascending. Doing that allows us to optimize the for loop and break since we know
# Values below a certain point cannot be considered. Still brute forced but better optimized

def getMoneySpent(keyboards, drives, s):
    if min(keyboards) > s or min(drives) > s:
        return -1
    keyboards.sort(reverse=True)
    drives.sort()

    total_list = []
    working_max = -1

    for k in keyboards:
        for l in drives:
            price = k + l
            if price == s:
                return s
            elif price > s:
                break
            else:
                if price > working_max:
                    working_max = price
    return working_max

s,n,m = raw_input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = map(int, raw_input().strip().split(' '))
drives = map(int, raw_input().strip().split(' '))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
