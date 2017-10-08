#!/bin/python

import sys

def solve(n, p):
    # Complete this function
    book_half = n/2

    # By default, start at page 1
    start_page = 1
    
    # If page is in second half of the book, it's better to start from the end
    if p > book_half:
        start_page = p

    flips = 0
    if start_page == 1: #Flip right
        current_page = 1
        if current_page == p:
            return 0
        while current_page < p:
            current_page += 2
            flips += 1
            if current_page % 2 != 0: # Page is on right so we need to check the left page as well
                if current_page == p or (current_page-1) == p: # No flips needed
                    return flips
    else:
        current_page = n
        if current_page % 2 != 0: # Final page is on right
            if current_page == p or (current_page-1) == p: # No flips needed
                return 0
        while current_page > p:
            current_page -= 2
            flips += 1
            if current_page % 2 != 0: # Page is on right so we need to check the left page as well
                if current_page == p or (current_page-1) == p: # No flips needed
                    return flips

    return flips

n = int(raw_input().strip())
p = int(raw_input().strip())
result = solve(n, p)
print(result)
