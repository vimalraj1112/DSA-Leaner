def ans():
    x=1221
    y=x
    rev=0

    while x>0:
        digit=x%10
        rev=(10*rev)+digit
        x=x//10

    if rev==y:
        return True
    else:
        return False

print(ans())        