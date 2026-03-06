def mer(a):
    mid=int(len(a)/2)
    c=[]
    i=0
    j=mid+1
    
    print(i,j,mid)
    while i<=mid and j<len(a):
        if a[i]<a[j]:
            c.append(a[i])
            i+=1
            

        else:
            c.append(a[j])
            j+=1
            

    while i<=mid:
        c.append(a[i])
        i+=1
        

    while j<len(a):
        c.append(a[j])
        j+=1
        

    return c  



print(mer([2,3,4,5,1,4,23]))    