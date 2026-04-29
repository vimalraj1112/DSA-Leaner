
def ans():
    n=1
    if n<0:
        return False
    if n<3:
        return True
    if n%2!=0:
        return False
    

    for i in range(n):
        if 2**i==n:
            return True
        if 2**i>n:
            return False
        
    return False
        
print(ans())        