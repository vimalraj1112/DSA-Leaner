def ans():

    s=['h','e','l','l','o']
    

    n=len(s)//2
    

    for i in range(n):
        x=len(s)-1-i
        temp=s[i]
        s[i]=s[x]
        s[x]=temp
        
        
        

    return s    

print(ans())
        