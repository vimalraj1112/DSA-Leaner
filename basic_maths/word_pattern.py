def ans():
    p = "abba"
    s = "dog cat cat dog"
    s=s.split()

    ans={}

    if len(p) != len(s):
        return False

    for i in range(len(p)):
        if p[i] in ans:
            if ans[p[i]] != s[i]:
                return False
            else:
                if  s[i] in ans.values():
                    return False
                ans[p[i]]=s[i]

    return True

print(ans())             