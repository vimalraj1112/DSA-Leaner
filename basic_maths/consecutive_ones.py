def ans():
    n=[1,1,0,1,1,1]

    x=len(n)
    c=0
    m=0

    for i in range(x):
        if n[i]==1:
            c+=1
        else:
            
            m=max(c,m)
            c=0
    return max(c,m)        
                

print(ans())            