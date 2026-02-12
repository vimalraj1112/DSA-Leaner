"""
def dif():
    n=5

    for i in range(n):
        for j in range(n-i):
            if j==0:
                print("A",end=" ")
            elif j==1:
                print("B",end=" ")    
            elif j==2:
                print("C",end=" ")    
            elif j==3:
                print("D",end=" ") 
            else:
                print("E",end=" ")    

        print()

dif()    """


def dif():
    n=5
    v=65
    
    

    for i in range(n):
        for j in range(i+1):
            x=chr(v)
            print(x,end=" ")
            
            v+=1

        print()
        v=65
        

dif()

