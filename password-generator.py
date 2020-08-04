#!/usr/bin/python3

import random
from random import shuffle
import clipboard



# Tasks:
# Handling odd char count : done
# Autocopy to clipboard : done
# Handle \\ properly for special char: pending
# Shuffle the final generated password : done

password=[]
caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=[0,1,2,3,4,5,6,7,8,9]
special=['~','!','@','#','$','%','^','&','*','(',')','-','>','<','?',':',';','"',"'",'}','{','[',']','\\','/']


def passgen(plen):
    global password, caps, small, num, special
    while 2 <= plen:
        if 0 < plen:
            rcap=random.choices(caps, k=2)
            password.extend(rcap)
            plen=plen-2
            if 0 < plen:
                rsmall=random.choices(small,k=2)
                password.extend(rsmall)
                plen=plen-2
                if 0 < plen:
                    rnum=random.choices(num, k=2)
                    password.extend(rnum)
                    plen=plen-2
                    if 0 < plen:
                        rspecial=random.choices(special, k=2)
                        password.extend(rspecial)
                        plen=plen-2
    return(password)

def oddevencheck(plen):
    global password, special
    if (plen % 2) == 0: # if even
        password=passgen(plen)
    else:               # if odd
        password=passgen(plen-1)
        rspecial=random.choices(special, k=1)
        password.extend(rspecial)
    return(shuffle(password))

if __name__ == "__main__":
    plen=input("[?] Enter password length: ")
    if int(plen) < 8:
        print("[~] Password cannot be less than 8 characters")
    else:
        oddevencheck(int(plen))
        clipboard.copy(''.join(str(p) for p in password))
        print("[>>>>] New password {} is copied to clipboard ".format(''.join(str(p) for p in password)))
