#!/usr/bin/env python

'''1.9 String Rotation: Assume you have a method isSubstring which checks
                        if one word is a substring of another. Given two
                        strings, s1 and s2, write code to check if s2 is
                        a rotation of s1 using only one call to isSubstring

'''

def isSubstring(s1, s2):
    return s2 in s1
    
def checkRotation(s1, s2):

    if len(s1) == len(s2) and len(s1) > 0:
        return isSubstring(s1+s1,s2)
        
    return False

if __name__ == '__main__':

    try:
        assert checkRotation('waterbottle', 'erbottlewat')
    except:
        raise AssertionError()
        
