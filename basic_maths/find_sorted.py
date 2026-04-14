
def ans():
    array=[]
    n=0
    
    for i in range(len(array)):
        if n<=array[i]:
           
            n=array[i]
        else:
            return False
        
    
    return True

print(ans())    
