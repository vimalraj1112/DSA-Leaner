def ans():
    w="abcde"

    d={}

    ans=0

    for i in w:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    f=sorted(d.values(),reverse=True)

    for i in range(len(f)):
        if i<=7:
            ans+=1
        if 7<i and 15>=i:
            ans+=2
        if 15<i and i>=23:
            ans+=3
        if i>23:
            ans+=4

    return ans

print(ans())                 