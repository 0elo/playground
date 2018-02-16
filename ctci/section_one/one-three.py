#!/usr/bin/env python

'''1.3 URLify: Write a method to replace all spaces in a string
               with '%20'. You may assume that the string has
               sufficient space at the end to hold the additional
               characters, and that you are given the "true" length
               of the string.

'''

def replaceStringEasy(input):
    return input.replace(' ', '%20')

def replaceString(input, trueLen):
    spaces = 0
    for i in range(trueLen):
        if input[i] == ' ':
            spaces += 1

    newLen = trueLen + (spaces * 2)
    newStr = [None]*newLen
    for i in reversed(range(trueLen)):
        if input[i] == ' ':
            newStr[newLen-1] = '0'
            newStr[newLen-2] = '2'
            newStr[newLen-3] = '%'
            newLen -= 3

        else:
            newStr[newLen-1] = input[i]
            newLen -= 1

    return ''.join(newStr)

if __name__ == '__main__':
    print(replaceStringEasy('Mr John Smith'))
    print(replaceString('Mr John Smith    ', 13))
