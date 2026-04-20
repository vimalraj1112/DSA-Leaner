def ans():
    p=[7,1,5,3,6,4]
    n=len(p)
    min=p[0]
    max=0
    
    for i in range(1,n):
        v=p[i]-min
        if max<v:
            max=v
        if p[i]<min:
            min=p[i]    
    
        

    return max

print(ans())            
                