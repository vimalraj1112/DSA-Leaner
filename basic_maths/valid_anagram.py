def ans():
    s = "a"
    t = "ab"

    x={}
    y={}

    if len(s)<len(t) or len(s)>len(t):
        return False

    for i in range(max(len(s),len(t))):  

        x[s[i]]=x.get(s[i],0)+1
        y[t[i]]=y.get(s[t],0)+1

    if x==y:
        return True
    else:
        return False        
        
        
print(ans())        


