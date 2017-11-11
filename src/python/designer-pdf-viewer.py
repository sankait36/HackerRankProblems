#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

letters = "abcdefghijklmnopqrstuvwxyz"
list_letters = list(letters)
dict_letters = {}

for x in range(0, len(h)):
    if list_letters[x] not in dict_letters:
        dict_letters[list_letters[x]] = h[x]

max_h = -1
list_word = list(word)
for letter in list_word:
    if dict_letters[letter] > max_h:
        max_h = dict_letters[letter]

print '%s' % (len(list_word)*max_h*1)

