def pat19():
    n=5
    x=0

    for i in range(n):
        for j in range(n-i):
            print("*",end=" ")
        for j in range(x):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")

        print()
        x+=2

    x=10
    for i in range(n):
        

        for j in range(i+1):
            print("*",end=" ")
        for j in range(2,x):
            print(" ",end=" ")

        for j in range(i+1):
            print("*",end=" ")

        print()
        x-=2    

pat19()                
