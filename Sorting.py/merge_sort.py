def mer(a,b):
    c=[]
    i=0
    j=0
    
    while i<len(a) and j<len(b):
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        
        else:
            c.append(a[i])
            i+=1
        

    while i<len(a):
        c.append(a[i])
        i+=1
        

    while j<len(b):
        c.append(b[j]) 
        j+=1
        


    return c      

print(mer([2,3,5,8],[1,4,23]))    