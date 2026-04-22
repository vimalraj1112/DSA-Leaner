

def ans():

    n=[0,1,0,3,12]
    x=0
    y=len(n)

    for i in range(y):
        if n[i] != 0:
            t=n[x]
            n[x]=n[i]
            n[i]=t
            x+=1
    
    return n

    

print(ans())        