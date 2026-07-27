from math import gcd

def ans():
    deck = [0,0,0,1,1,1,2,2,2]

    d={}

    for i in deck:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    v=list(d.values())

    g=v[0]

    for i in v[1:]:
        g=gcd(g,i)

    if g>=2:
        return True

    return False 



print(ans())            