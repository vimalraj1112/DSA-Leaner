def sel(a):
    for i in range(len(a)-1):
        min_val=i
        for j in range(i,len(a)):
            if a[min_val]>a[j]:
                min_val=j
        if i!=min_val:
            temp=a[i]
            a[i]=a[min_val]
            a[min_val]=temp

    return a        

            

print(sel([5,4,3,2,1]))   
