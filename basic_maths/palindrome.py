x=121
v=x
rev=0

while x>0:
    digit=x%10
    rev=rev*10+digit
    x=x//10

if v==rev:
    print(True)
else:
    print(False)        