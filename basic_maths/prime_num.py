#Check if a number is prime or not

from math import *
def prime(n):
    
    count=0
    #edge case
    if n<4:
        return True
    if n%2==0:
        return False

    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            count+=1
            if count==2:
                break
    if count==2:
        return False
    else:
        return True

print(prime(2))       

                


