def ans():
    s = "abccccdd"

    d={}
    odd=False
    a=0

    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    f=dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

    for c in d.values():
        if c%2==0:
            a+=c
        else:
            a+=c-1
            odd=True

    if odd:
        a+=1                 
    return a

print(ans())    