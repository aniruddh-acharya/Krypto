
#caesar cipher
def encrypt(a,k):
    k = int(k)
    l=[]
    for i in a:
        if i.isalpha():
            if i.isupper():
                l.append(chr(((ord(i)-65+k)%26)+65))
            else:
                l.append(chr(((ord(i)-97+k)%26)+97))
        else:
            l.append(i)
    return ''.join(l)        

def decrypt(a,k):
    k = int(k)
    l=[]
    for i in a:
        if i.isalpha():
            if i.isupper():
                l.append(chr(((ord(i)-65-k)%26)+65))
            else:
                l.append(chr(((ord(i)-97-k)%26)+97))
        else:
            l.append(i)
    return ''.join(l)  
