n=int(input("enter the number:"))

i=0

if n==0:
    i=1

while n>0:
    n=n//10
    i+=1

print(i)    


