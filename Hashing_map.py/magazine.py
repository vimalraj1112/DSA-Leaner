def ans():

    r='aa'
    m='ab'

    d={}

    for i in m:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in r:
        if d[i]==0:
            return False
        if i in d:
            d[i]-=1
            
        else:
            return False

    return True      

print(ans())              