def ans():
    s = "f11"
    t = "a23"

    dic={}
    
    for i in range(len(s)):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        else:
            if t[i] in dic.values():
                return False
            dic[s[i]]=t[i]
    return True

print(ans())        