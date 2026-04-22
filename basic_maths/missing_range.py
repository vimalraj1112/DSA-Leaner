def ans():
    n=[3,0,1]

    x=len(n)

    for i in range(x-1,0,-1):
        if i != n[i]:
            return i
        

print(ans())        