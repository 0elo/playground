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

oneAway('pale', 'bale')
try:
	
	assert oneAway('pale', 'ple')
	print 'pass'
	assert oneAway('pales', 'pale')
	print 'pass'
	assert oneAway('pale', 'bale')
	print 'pass'
	assert oneAway('pale', 'labe')
	assert oneAway('rips', 'ips')
	assert oneAway('ips', 'mips')
	assert oneAway('lips', 'tips')
	
except:

	raise AssertionError()