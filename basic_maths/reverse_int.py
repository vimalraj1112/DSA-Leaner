def ans():
    n=-123

    x=n
    if n<0:
        n=n*-1
    rev=0

    while n>0:
        digit=n%10
        rev=(10*rev)+digit
        n=n//10
    if x<0:
        return -rev
    else:
        return rev

print(ans())    