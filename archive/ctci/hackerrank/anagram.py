#!/usr/bin/python

'''
Implementations for finding number of letters that need
to be removed from two strings to make them anagrams
from HackerRank problem:
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

Inputs: <string> first string
        <string> second string
'''

def numbersNeededCounter(a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return sum(abs(a.count(letter) - b.count(letter)) for letter in alphabet)

def numbersNeededHashTable(a, b):
    letters_dict = dict.fromkeys(a + b, 0)
    for letter in a:
        letters_dict[letter] += 1
    for letter in b:
        letters_dict[letter] -= 1
    return sum([abs(count) for count in letters_dict.values()])
