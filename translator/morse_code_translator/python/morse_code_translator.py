#Morse Code to English - English to Morse Code translator 


#!/usr/bin/python
import sys
import __builtin__
import string


CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': '/'
        }

CODE_REVERSED=dict((v,k) for (k,v) in CODE.items())
msg = raw_input('MESSAGE: ')



def main():
 if msg[0][0]=='.' or msg[0][0]=='-':
         return morseToEng()
        else:
         return engToMorse()

def engToMorse():
 link='. Check the translation in my CodePen! @Meli94'
 newmsg= ' '.join(CODE[char.upper()] for char in msg) #sentence translated (From english to Morse)

 mess= newmsg 
 print mess
 
def morseToEng():

         print ''.join(CODE_REVERSED.get(i) for i in msg.split())



if __name__ == "__main__":
        main()
