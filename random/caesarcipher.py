#!/usr/bin/python

'''
February challenge from py-study-group/challenges:
Caesar cipher encoder/decoder (Advanced)

Link: https://github.com/py-study-group/challenges/tree/master/February

'''

import argparse, os
from pathlib import Path
from langdetect import detect
from polyglot.text import Text

#__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

__location__ = Path.cwd()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_LEN = 26
ASCII = [65, 90, 97, 122]
COMMON_LETTERS = 'etaoinsrhldcumfpgwybvkxjqz'

class Cipher:
    '''Represents the message to be encoded/decoded.
    This class is used to encode and decode messages.

    Attributes:
        string (str): The message to be encoded/decoded.
        shift  (int): The amount to shift the message by.

    '''
    
    def __init__(self, string: str, shift: int = 0):
        '''This is the __init__ method.

        Args:
            string (str): The message to be encoded/decoded.
            shift (int, optional): The amount to shift the message by.

        '''
        self.string = string
        self.shift = shift
        self.encoded = ''
        self.decoded = ''

    def printEncodedHash(self):
        '''Prints the encoded string using hash table implementation.

        '''

        # If this is an empty string, run encodeHashTable()
        # to set encoded string to self.encoded
        if not self.encoded:
            self.encodeHashTable()

        print(self.encoded)

        
    def printDecodedHash(self):
        '''Prints the decoded string using hash table implementation.

        '''
        
        # If this is an empty string, run decodeHashTable()
        # to set decoded string to self.decoded
        if not self.decoded:
            self.decodeHashTable()
            
        print(self.decoded)

    def cleanString(self, string: str) -> str:
        '''Clears input string of non alphabetical characters

        Args:
            string (str): The string to be cleaned

        '''
        cleaned = ''.join([i for i in string.lower() if i.isalpha()])

        return cleaned

    def detectEnglish(self, string: str) -> bool:
        '''Detects if a string is English by checking
        against polyglot and langdetect libraries.

        Current solution to detect if string is English
        is to check against both langdetect and polyglot.
        Longer sentences are split by every ten words and
        verified via polyglot a second time.

        Will make solution more robust following extensive testing.

        Args:
            string (str): The string to be analyzed
        
        '''
        text = Text(string)
        if detect(string) == 'en' and text.language.code == 'en':
            textSplit = text.split(' ')
            words = []
            temp = []
            counter = 0
            modNum = 10
            remaining = 0
            
            for idx, i in enumerate(textSplit):
                temp.append(i)
                remaining += 1
                if ((idx+1) % modNum) == 0:
                    words.append(temp)
                    remaining = 0
                    temp = []
            if temp:
                if remaining < (modNum/2):
                    words[-1].extend(temp)
                else:
                    words.append(temp)

            for group in words:
                if Text(' '.join(group)).language.code != 'en':
                    return False
            return True
        return False

    def printPrediction(self):
        '''Prints prediction of the shift and decoded string.

        '''
        guess, original, decoded = self.detectByFrequency()
        
        print('\nOriginal string:\n{}'.format(original))
        print('\nPredicted shift of: {}'.format(guess))
        print('\nDecoded string:\n{}\n'.format(decoded))
    
    def detectByFrequency(self):
        '''Detects whether a string is English via frequency analysis.

        '''

        # If the string is already English, just
        # return the string
        if self.detectEnglish(self.string):
            return(0,self.string,self.string)
        #temp = self.string
        #cleaned = self.cleanString(temp)
        cleaned = self.cleanString(self.string)
        letters = dict.fromkeys(cleaned, 0)
        for letter in self.string.lower():
            if letter in letters:
                letters[letter] += 1

        swapList = sorted(letters.items(), reverse=True)
        swapList = swapList[:7]
        for swap in COMMON_LETTERS:
            for pair in swapList:
                swapee = pair[0]
                if ord(swapee) > ord(swap):
                    guess = 26 - (ord(swapee) - ord(swap))
                else:
                    guess = (ord(swap)-ord(swapee))
                    
                guessValues = ALPHABET[-guess:] + ALPHABET[:-guess]
                decodeMap = dict(zip(ALPHABET, guessValues))

                decoded = ''.join([decodeMap[i.lower()].upper() if i.lower() in decodeMap and i.isupper() else decodeMap[i] if i in decodeMap else i for i in self.string])
                if self.detectEnglish(decoded):
                    return(guess,self.string,decoded)

        return(0,self.string,'Could not determine')
        
    def encodeHashTable(self):
        '''Encodes message using a hash table implementation.
        
        Returns:
            str: Encoded message.

        '''
        encodedValues = ALPHABET[self.shift:] + ALPHABET[:self.shift]
        encodeMap = dict(zip(ALPHABET, encodedValues))
        self.encoded = ''.join([encodeMap[c] if c.islower() else encodeMap[c.lower()].upper() if c.lower() in encodeMap else c for c in self.string])
        #return('Encoded string:\n{}\n'.format(self.encoded))

    def decodeHashTable(self):
        '''Decodes message using a hash table implementation.

        Returns:
            str: Decoded message.

         '''
        decodedValues = ALPHABET[-self.shift:] + ALPHABET[:-self.shift]
        decodeMap = dict(zip(ALPHABET, decodedValues))
        self.decoded = ''.join([decodeMap[c] if c.islower() else decodeMap[c.lower()].upper() if c.lower() in decodeMap else c for c in self.string])
        #return('Decoded string:\n{}\n'.format(self.decoded))
    
    def encodeOrdinal(self):
        '''Encodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Encoded message.

        '''
        return('Encoded sentence:\n{}\n'.format(''.join([chr(ord(c)+self.shift) if ( (c.isupper() and (ord(c)+self.shift >= ASCII[0] and ord(c)+self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift >= ASCII[2] and ord(c)+self.shift <= ASCII[3]) ) ) else chr(ord(c)+self.shift-ALPHABET_LEN) if ( (c.isupper() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[0] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)+self.shift-ALPHABET_LEN >= ASCII[2] and ord(c)+self.shift-ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))
        
    def decodeOrdinal(self):
        '''Decodes message using ordinals, with the ugliest possible list comprehension.

        Returns:
            str: Decoded message.

        '''
        return('Decoded sentence:\n{}\n'.format(''.join([chr(ord(c)-self.shift) if ( (c.isupper() and (ord(c)-self.shift >= ASCII[0] and ord(c)-self.shift <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift >= ASCII[2] and ord(c)-self.shift <= ASCII[3]) ) ) else chr(ord(c)-self.shift+ALPHABET_LEN) if ( (c.isupper() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[0] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[1]) ) or (c.islower() and (ord(c)-self.shift+ALPHABET_LEN >= ASCII[2] and ord(c)-self.shift+ALPHABET_LEN <= ASCII[3]) ) ) else c for c in self.string])))


class handleArgs:

    def __init__(self):
        # This is the init method.

        self.encodeFlag = False
        self.decodeFlag = False
        self.handleDetect = False
        self.handleFile = False
        self.handleText = False
        self.shift = 0
        self.string = ''
        self.conversion = ''
            
    def getShift(self):
        # Accessor for shift
        return self.shift

    def getString(self):
        # Accessor for input string
        return self.string

    def printString(self):
        return 'Original message: {}'.format(self.string)
        
    def getArgs(self):

        # Top level arg handler with program description
        parser = argparse.ArgumentParser(description='This is a multifunctional Caesar cipher tool written in Python 3.6. The detect command takes an string encrypted by a Caesar cipher with an unknown shift, and makes a prediction of the how the string was encoded. The file and string commands call functionality to encode or decode a string by a user-specified shift. The string can be read in from the command line or a file.')

        # Add subparsers for the Detect, File, and Text commands
        subparser = parser.add_subparsers(dest='selection', help = 'Select from {detect, file, text}')
        subparser.required = False
        
        # Detect Command
        detect_command = subparser.add_parser('detect', help='Detect shift of an encoded string')
        detect_command.add_argument('d_file', action='store', help='File to be decoded')

        # File Command
        file_command = subparser.add_parser('file', help='File to be encoded or decoded')
        file_command.add_argument('f_conversion', action='store', help="Choose to 'encode' or 'decode' the string", type=str)
        file_command.add_argument('f_shift', action='store', help='Shift the string by this amount', type=int)
        file_command.add_argument('thefile', action='store', help='File containing string to be encoded or decoded', type=str)
        
        # Text Command
        text_command = subparser.add_parser('text', help='String to be encoded or decoded')
        text_command.add_argument('t_conversion', action='store', help="Choose to 'encode' or 'decode' the string", type=str)
        text_command.add_argument('t_shift', action='store', help='Shift the string by this amount', type=int)
        text_command.add_argument('thetext', action='store', help='Text to be encoded or decoded', type=str)

        # Stores args into dict
        args = vars(parser.parse_args())

        # Set appropriate values if Detect command selected
        if args['selection'] == 'detect':

            self.handleDetect = True

            # Parse file and set as input string
            if Path(args['d_file']).is_file():
                theFile = open(Path(__location__ / args['d_file']), 'r')
                self.string = ''.join([line for line in theFile])
                theFile.close()

            else:
                parser.error('Could not locate file!')
                
            self.conversion = 'decode'

        # Set appropriate values if File command selected    
        elif args['selection'] == 'file':
            
            self.conversion = args['f_conversion']
            self.handleFile = True
            self.shift = args['f_shift']

            # Parse file and set as input string
            if Path(args['thefile']).is_file():
                theFile = open(Path(__location__ / args['thefile']), 'r')
                self.string = ''.join([line for line in theFile])
                theFile.close()
                
            else:
                parser.error('Could not locate file!')

        # Set appropriate values if Text command selected
        elif args['selection'] == 'text':
            self.conversion = args['t_conversion']
            self.handleText = True
            self.shift = args['t_shift']
            self.string = args['thetext']
        
        else:
            ''' Runs if no command line args are provided.

            Prompts user for input words, the option to encode or decode,
            and the value to shfit by. The resulting encoded/decoded string
            is printed.
            '''

            # Get what the user wants
            self.string = input('Please enter a sentence: ').strip()

            # Get encode or decode
            conversionType = input('Enter (encode or decode): ').strip()

            # Validate that encode or decode was provided as input
            while conversionType != 'encode' and conversionType != 'decode':

                conversionType = input('Enter (encode or decode): ').strip()

            # Assign conversion type
            self.conversion = conversionType

            # Validate that input shift is an int
            while True:
                shiftNum = input('Please enter a shift amount: ').strip()

                try:
                    
                    shiftNum = int(shiftNum)
                    break;
                    
                except ValueError:
                    print('This is not a number')

            # Assign shift
            self.shift = shiftNum

        # Set encode and decode flags
        if self.conversion == 'encode':
            
            self.encodeFlag = True

        elif self.conversion =='decode':

            self.decodeFlag = True

        else:

            # Error checking if encoding/decoding not specified as cmd line arg
            parser.error("Enter 'encode' or 'decode' for the conversion argument!")

        # If the shift is greater than the length of the alphabet,
        # that's the same as the modulus of the shift and alphabet length.
        if ALPHABET_LEN < self.shift:

            self.shift = self.shift % ALPHABET_LEN

            
if __name__ == '__main__':

    # Masthead
    print('\n{}\n        Z E R O E L O \' S\n    C A E S A R   C I P H E R\n{}\n'.format('*'*36,'*'*36))
    
    args = handleArgs()
    args.getArgs()
    
    message = Cipher(args.getString(), args.getShift())

    if args.handleDetect:
        message.printPrediction()
    else:
        if args.encodeFlag:
            message.printEncodedHash()
        else:
            message.printDecodedHash()
