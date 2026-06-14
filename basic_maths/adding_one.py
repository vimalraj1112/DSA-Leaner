def ans():
    n=[9,9,9]

    for i in range(len(n)-1,-1,-1):
        if n[i]==9:
            n[i]=0
        else:
            n[i]+=1
            return n
        
    return [1]+n 

print(ans())   
