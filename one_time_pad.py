import random


def encrypt(m,k):
    m = toBin(m)
    c = ''.join(list(map(lambda a,b:str(int(a)^int(b)),m,k)))
    return toStr(c)
    

def decrypt(c,k):
    c = toBin(c)
    m = ''.join(list(map(lambda a,b:str(int(a)^int(b)),c,k)))
    return toStr(m)
    
    
def toBin(t):
    s = ''.join(list(map(lambda a: filler(bin(ord(a))[2:],8),t)))
    return s

def toStr(b):
    m = ''
    i = 0
    f = 8
    for j in range(len(b)//8):
        m += chr(toDec(b[i:f]))
        i+=8
        f+=8
    return m
        

def generate_key(m):
    m = toBin(m)
    l = len(m)
    k = ''
    for i in range(l):
        k+=random.choice(['0','1'])
    return k

        
def filler(b,n):
    if(len(b)==n):
        return b
    else:
        tp = n-len(b)
        b = ('0'*tp) + b
        return b

def toDec(b):
    l = list(map(lambda a,c:int(a)*(2**c),b[::-1],range(len(b))))
    return sum(l)

