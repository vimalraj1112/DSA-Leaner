def ans():
    n=7

    a=0

    for i in range(1,n):
        if n%2==0:
            if i%2!=0:
                if n%i==0:
                    a+=1
                    n-=i
        if n%i==0:
            a+=1
            n-=i

    print(a)
    if a%2==0:
        return False
    return True

print(ans())        