#!/usr/bin/env python

'''1.1 Is Unique: Implement an algorithm to determine if a string has all unqiue characters

'''

import string

def isUnique(input):
    # Assume 128-character alphabet
    charset = 128

    if len(input) > charset:
        return False

    map = dict.fromkeys(input, 0)

    for character in input:
        if not map[character]:
            map[character] += 1
        else:
            return False

    return True

if __name__ == '__main__':
    try:
        assert isUnique(string.ascii_uppercase + string.ascii_lowercase)
        assert isUnique(string.printable)
        assert not isUnique(string.printable*2)
        assert not isUnique('abcABCabcABC')
        
    except:

        raise AssertionError()
