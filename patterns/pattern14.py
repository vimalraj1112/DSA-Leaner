def abc():
    n=5

    for i in range(n):
        for j in range(i+1):
            if j==1:
                print("B",end=" ")
            elif j==2:
                print("C",end=" ") 
            elif j==3:
                print("D",end=" ")      
            elif j==4:
                print("E",end=" ")        
            else:
                print("A",end=" ")
        print()

abc()            