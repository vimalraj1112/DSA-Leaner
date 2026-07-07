def ans():
    s = "ab"
    g = "ba"

    if len(s) != len(g):
        return False
    if s==g:

        if len(s) == len(set(s)):
            return False
        return True
    
    ind=[]
    for i in range(len(s)):
        if s[i]!=g[i]:
            ind.append(i)
            if len(ind)>2:
                return False
    if len(ind)==2:
        if s[ind[0]]==g[ind[1]] and s[ind[1]]==g[ind[0]]:
            return True
    return False     

print(ans())           

