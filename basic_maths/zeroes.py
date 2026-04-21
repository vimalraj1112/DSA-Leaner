

def ans():

    n=[0,1,0,3,12]

    x=len(n)

    for i in range(x):
        if n[i]==0:
            n.remove(n[i])
            n.append(0)
    
        
              
            

    return n

    

print(ans())        