def ans():
    s = "abcd"
    t = "abcda"

    d={}
    a=[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    for i in t:
        if i not in d:
            return i
        if i in d:
            d[i]-=1

        if d[i]<0:
            return i                
                
print(ans())