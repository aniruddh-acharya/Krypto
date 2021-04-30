#a = int(input("Enter the value of a "))
#b = int(input("Enter the value of b "))
#msg = input("Enter the message to be encrypted ")

d = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
def encrypt(msg,a):
    a = int(a)
    b = a+3
    msg = msg.lower()
    s = ""
    for i in msg:
        if(i in d.keys()):
            f = (a*d[i]+b)%26
            for j in d:
                if(d[j] == f):
                    s = s + j
        else:
            s = s+i
    return s


def decrypt(txt,a):
    a = int(a)
    b = a+3
    txt = txt.lower()
    msg = ""
    inverse = 0
    for i in range(26):
        if((a*i)%26 == 1):
            inverse = i
    for i in txt:
        if(i in d.keys()):
            f = inverse*(d[i]-b)%26
            for j in d:
                if(d[j] == f):
                    msg = msg + j
        else:
            msg = msg+i
    return msg
        
