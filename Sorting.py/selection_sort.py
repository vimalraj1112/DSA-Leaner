import array
def rel(a):

    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                temp=a[j]
                temp1=a[i]
                a[i]=temp
                a[j]=temp1
    return a
             
print(rel([13,46,24,52,20,9]))
