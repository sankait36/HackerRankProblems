from itertools import combinations

def  buildSubsequences(s):
    subsquences = []
    for x in range(1, len(s) + 1):
        comb =  combinations(s, x)
        for val in comb:
            subsquences.append(''.join(val))
    subsquences.sort()
    print subsquences
s = raw_input().strip()
buildSubsequences(s)
