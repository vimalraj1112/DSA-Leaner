def pat11():

    n=5
    a=1

    for i in range(n):
        if i%2==0:
            a=1
        else:
            a=0    
        for j in range(i+1):
            print(a,end=" ")
            a=1-a
                
            
        print()

pat11()  




def ex():
    n=5

    for i in range(n):
        for j in range(i+1):
            x=i+j
            if x%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")


        print()


ex()