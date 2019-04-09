#!/usr/bin/env python

'''1.4 Palindrome Permutation: Given a string, write a function to
                               check if it is a permutation of a
                               palindrome. A palindrome is a word
                               or phrase that is the same forwards
                               and backwards. A permtuation is a 
                               rearrangement of letters. The palindrome
                               does not need to be limtied to just
                               dictionary words.

'''

def checkPalindrome(input):

	map = {}
	
	for i in input:
		if i.isalpha():
			if i.lower() in map:
				map[i.lower()] += 1
			else:
				map[i.lower()] = 1
	
	oddFlag = False
	
	for i in map:
		if map[i] % 2 != 0:
			if (oddFlag):
				return False
			oddFlag = True
	return True

if __name__ == '__main__':

        try:

	        assert checkPalindrome('A but tuba')
	        assert checkPalindrome('battubua')
	        assert checkPalindrome('aladnamedmandalae')
	        assert checkPalindrome('nasatatanasa')
	        assert not checkPalindrome('azzzkfkfabab')
	        assert checkPalindrome('azzzkfkfabb')
	        assert checkPalindrome('Alletsdellacalledstella')
	
        except:

	        raise AssertionError()
	
