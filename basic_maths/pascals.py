def ans():
    r=3
    ans=[[1]]

    for i in range(r):
        n=[1]
        p=ans[-1]
        for j in range(len(p)-1):
            n.append(p[j]+p[j+1])
        n.append(1)
        ans.append(n)

    return ans[-1]      

print(ans())  