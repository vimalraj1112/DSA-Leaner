"""
def pat21():
    n=4

    for i in range(n):
        if i==0 or i==n-1:

            for j in range(n):
                print("*",end=" ")

            print()    

        else:

            for j in range(n-3):
                print("*",end=" ")

            for j in range(n-2):
                print(" ",end=" ")

            for j in range(n-3):
                print("*",end=" ")

            print()        

pat21() """


def pat():
    n=4

    for i in range(n):
        for j in range(n):
            if i==0 or j==3 or i==3 or j==0:
                print("*",end=" ")
            else:
                
                print(" ",end=" ")

        print()

pat()


        