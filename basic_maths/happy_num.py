def ans():
    n=19
    ans=0
    seen=set()
    while n!=1:
        for digit in str(n):
            ans+=int(digit)**2 
        n=ans
        ans=0
        if n in seen:
            return False
        
        seen.add(n)
    
    return True
    
print(ans())    
