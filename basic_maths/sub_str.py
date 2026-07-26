def ans():
    s="acb"
    t="ahcgdb"
    a=0
    for i in t:
        if a<len(s) and s[a]==i:
            a+=1

    if a==len(s):
        return True
    return False             

print(ans())      
