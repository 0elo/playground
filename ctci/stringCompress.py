def stringCompress(input):

	consec = 0
	compressed = ''
	
	for i in range(len(input)):
		
		consec += 1
		
		if ( (i + 1 >= len(input) ) or (input[i] != input[i+1])):
			compressed += input[i] + str(consec)
			consec = 0
			
	return compressed		
	
print stringCompress('aabcccccaaa')