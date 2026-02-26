import array
def bub(a):

    for i in range(len(a)-1,0,-1):
        for j in range(0,i):
            if a[j]>a[j+1]:
                temp=a[j+1]
                temp1=a[j]
                a[j]=temp
                a[j+1]=temp1

    return a
print(bub([13,46,24,52,20,9]))            