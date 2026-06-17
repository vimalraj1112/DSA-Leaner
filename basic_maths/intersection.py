def ans():
    n1 = [1,2,2,1] 
    n2 = [2,2,1,1]
    ans=set()

    n=set(n1)

    for i in n:
        if i in n2:
            ans.add(i)

    return list(ans)
print(ans())
