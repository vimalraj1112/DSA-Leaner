from array import *
v=array('i',[])
def rev(arr):
    global v
    if len(v)==len(a):
        return v
    ind=len(a)-len(v)-1
    v.append(arr[ind])
    return rev(arr)

a=array('i',[1,2,3,4,5])
print(rev(a))        