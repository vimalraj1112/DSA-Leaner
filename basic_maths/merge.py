n1=[1,2,3,0,0,0]
n2=[2,4,5]

x=len(n1)
m=3
n=3
pt=m+n

while 0<n and 0<m:
    if n2[n-1]>n1[m-1]:
        n1[pt-1]=n2[n-1]
        pt-=1
        n-=1
    else:
        n1[pt-1]=n1[m-1]
        pt-=1
        m-=1

print(n1)        

    

    

       