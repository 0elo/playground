#!/usr/bin/env python

'''1.6 String Compression: Implement a mehtod to perform basic string compression
                           using the coutns of repeated characters. For example,
                           the string aabcccccaaa would become a2b1c5a3. If the
                           "compressed" string would not become smaller than the
                           original string, your method should return the original
                           string. You can assume the string has only uppercase and
                           lowercase letters (a-z).

'''

def stringCompress(input):

	consec = 0
	compressed = ''
	
	for i in range(len(input)):
		
		consec += 1
		
		if ( (i + 1 >= len(input) ) or (input[i] != input[i+1])):
			compressed += input[i] + str(consec)
			consec = 0
			
	return compressed		

if __name__ == '__main__':
        print(stringCompress('aabcccccaaa'))
