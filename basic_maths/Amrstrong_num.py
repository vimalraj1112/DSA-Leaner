n=153
comp=n
m=str(n)
x=0


total=0

for i in range(len(m)):
    x=n%10
    n=n//10
    total+=x**len(m)


if comp==total:
    print(True)
else:
    print(False)
