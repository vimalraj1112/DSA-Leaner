def pat9():
    n=5

    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(2*i+1):
            print("*",end=" ")
        print()

    for i in range(n):    
        for j in range(i+1):
            print(" ",end=" ")
        for j in range((n*2)-(2*i)-1):
            print("*",end=" ")
        
        print()


pat9()               