v=[]
def pal(lis):
    global v
    if len(lis)==0:
        return v
    ind=len(lis)-1
    v.append(lis[ind])
    lis.pop(ind)
    return pal(lis)
    
a=['r','a','c','e','c','a','r'] 

string1=''.join(pal(a.copy()))
string2=''.join(v)

if string1==string2:
    print("its palindrome")
else:
    print("not yet")