def ans():
    n=5

    ans=[[1]]

    for i in range(1,n):
        p=ans[-1]
        n=[1]
        for j in range(len(p)-1):
            n.append(p[j]+p[j+1])
        n.append(1)
        ans.append(n)

    return ans

print(ans())    