def ans():
    n=15
    m=4

    ans=[]

    for i in range(20,-1,-1):
        if i%m==0:
            ans.append(i)

            

    return ans

print(ans())    

