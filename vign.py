
#Dont run this. DONT.
def key(string, key):
    s = ""; i = 0 
    while(len(s) != len(string)):
        s += key[i%len(key)]
        i+=1
    return s

#Just run this for cipher.
def encrypt(string, key1):
    string = string.upper()
    key1 = key1.upper()
    key_ = key(string,key1)
    cipher = ""
    for i in range(len(key_)):
        if(string[i] != ' '):
            p = (ord(string[i]) + ord(key_[i]))%26
            p += ord('A')
            cipher += chr(p)
        else:
            cipher += ' '
    return cipher
#Run to decipher. 
def decrypt(string, key1):
    string = string.upper()
    key1 = key1.upper()
    key_ = key(string, key1)
    res = ""
    for i in range(len(string)):
        if(string[i] != ' '):
            p = (ord(string[i]) - ord(key_[i]) + 26)%26
            p += ord('A')
            res += chr(p)
        else:
            res += ' '
    return res



