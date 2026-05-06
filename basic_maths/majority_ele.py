from math import *

def ans():
    n=[3,2,3,2,2,5,5,5]

    x={}
    y=ceil(len(n)/2)

    for i in n:
        if i in x:
            x[i]+=1
        else:
            x[i]=1
        if x[i]==y:
            return i    

print(ans())    