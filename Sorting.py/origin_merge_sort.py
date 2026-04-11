def rec(a,low,high):
    if low==high:
        return
    mid=(low+high)//2

    rec(a,low,mid)
    rec(a,mid+1,high)
    mer(a,low,mid,high)
    return a




def mer(a,low,mid,high):
    i=low
    j=mid+1
    temp=[]
    while i<=mid and j<=high:
        if a[i]>a[j]:
            temp.append(a[j])
            j+=1

        else:
            temp.append(a[i])
            i+=1

    while i<=mid:
        temp.append(a[i])
        i+=1

    while j<=high:
        temp.append(a[j])
        j+=1
        

    for i in range(low,high+1):
        a[i]=temp[i-low]



print(rec([5,4,3,2,1],0,4))               


