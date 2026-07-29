def ans():
    n=[0,0,1,1,1,1,2,3,3]

    i=2

    for j in range(2,len(n)):
        if n[i-2]!=n[j]:
            n[i]=n[j]
            i+=1

    return i        


     

print(ans())              