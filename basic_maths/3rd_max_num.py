def ans():
    n=[2,3,3,2]

    n=set(n)
    n=list(n)
    n.sort()

    if len(n)<3:
        return n[len(n)-1]
    
    return n[len(n)-3]
        
print(ans())    