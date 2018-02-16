#!/usr/bin/env python

'''1.5 One Away: There are three types of edits that can be performed
                 on strings: insert a character, remove a character,
                 or replace a character. Given two strings, write a
                 function to check if they are one edit (or zero edits) away.

'''

def oneAway(first, second):
	if first == second:
		return True
	
	oddFlag = False
	
	if len(first) > len(second):
		map = dict.fromkeys(first, 0)
		for i in first:
			map[i] += 1
		for j in second:
			if j in map:
				map[j] -= 1
			else:
				if oddFlag:
					return False
				oddFlag = True


	else:
		map = dict.fromkeys(second, 0)
		for i in second:
			map[i] += 1
		for j in first:
			if j in map:
				map[j] -= 1
			else:
				if oddFlag:
					return False
				oddFlag = True

	return (sum([map[i] for i in map]) <= 1)

if __name__ == '__main__':
        try:
	        
	        assert oneAway('pale', 'ple')
	        assert oneAway('pales', 'pale')
	        assert oneAway('pale', 'bale')
	        assert oneAway('pale', 'labe')
	        assert oneAway('rips', 'ips')
	        assert oneAway('ips', 'mips')
	        assert oneAway('lips', 'tips')
	
        except:

	        raise AssertionError()
