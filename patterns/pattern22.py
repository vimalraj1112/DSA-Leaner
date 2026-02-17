
def final():
    n=7

    for i in range(n):
        for j in range(n):
            if i==0 or j==6 or i==6 or j==0:
                print(n-3,end=" ")
            elif i==1 or j==5 or i==5 or j==1:
                print(n-4,end=" ")
            elif i==2 or j==4 or i==4 or j==2:
                print(n-5,end=" ")    
            else:
                print(n-6,end=" ")    
        print()

final()   


         