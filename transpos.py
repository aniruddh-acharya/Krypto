#transposition cipher
def encrypt(s,key):
    key = int(key)
    ci=['']*key
   
    for col in range(key):
        p=col

        while p<len(s):
            ci[col]+=s[p]
            p+=key
   
    return ''.join(ci)      

import math
def decrypt(message,key):
    key = int(key)
    
    numOfColumns = math.ceil(len(message) / key)
    
    numOfRows = key
    
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

   
    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)

