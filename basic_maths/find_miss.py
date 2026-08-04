def ans():
    n=[5,1]

    s=min(n)
    l=max(n)

    ans=[]

    for i in range(s,l+1):
        if i not in n:
            ans.append(i)    

    return ans

print(ans())        