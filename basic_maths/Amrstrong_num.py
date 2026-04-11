n=int(input("enter the number:"))
comp=n
s=str(n)
x=0
total=0

for i in range(len(s)):
    x=n%10
    n=n//10
    total+=x**len(s)
    

if comp==total:
    print(True)
else:
    print(False)    