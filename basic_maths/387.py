def ans():
    s="loveleetcode"
    
    d={}

    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1

    for i in d:
        if d[i] == 1:
            return s.index(i)     

    return -1

print(ans())            