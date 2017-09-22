#!/bin/python

import sys

def solve(grades):
    # Complete this function
    rounded_grades = grades
    for x in range(0, len(rounded_grades)):
        if rounded_grades[x] >= 38:
            mod = (rounded_grades[x] % 5)
            if mod == 3:
                rounded_grades[x] += 2
            if mod == 4:
                rounded_grades[x] += 1

    return rounded_grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
#print "\n".join(map(str, result))