x=int(input('enter the number:'))
s=x
rev=0

while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10

if s==rev:
    print(True)
else:
    print(False)  

    


