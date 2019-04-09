#!/usr/bin/env python

'''1.2 Check Permutation: Given two strings, write a method to decide
                          if one is a permutation of the other

'''

def checkPermutation(first, second):

    if len(first) != len(second):
        return False

    map = dict.fromkeys(first, 0)
    
    for i in first:
        map[i] += 1
    for j in second:
        if i in map:
            map[j] -= 1
            if map[j] < 0:
                return False

        else:
            return False

    return not sum(count for count in map.values())

if __name__ == '__main__':
    try:
        assert not checkPermutation('god    ', 'dog')
        assert checkPermutation('god', 'ogd')
        assert checkPermutation('AllmyfriendsareDEAD', 'lmlyDrearADieEdAsnf')

    except:
        raise AssertionError()
