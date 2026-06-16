def ans():
    p=[[0,0],[1,0],[2,0]]
    ans=0

    for i in range(len(p)):
        d={}
        for j in range(len(p)):
            if i==j:
                continue
            dx=p[i][0]-p[j][0]
            dy=p[i][1]-p[j][1]

            a=dx*dx + dy*dy

            d[a]=d.get(a,0)+1

        for m in d.values():
            ans+=m*(m-1)

    return ans

print(ans())            