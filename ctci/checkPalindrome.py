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
	
try:

	assert checkPalindrome('A but tuba')
	assert checkPalindrome('battubua')
	assert checkPalindrome('aladnamedmandalae')
	assert checkPalindrome('nasatatanasa')
	#assert checkPalindrome('azzzkfkfabab')
	assert checkPalindrome('azzzkfkfabb')
	assert checkPalindrome('Alletsdellacalledstella')
	print 'All were palindromes'
	
except:

	raise AssertionError()
	
