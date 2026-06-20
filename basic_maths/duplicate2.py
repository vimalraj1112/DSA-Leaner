def ans():
    n=[1,2,3,1]
    k=3
    d={}

    for i in range(len(n)):
        if n[i] in d:
            if abs(d[n[i]]<=k):
                return True
        d[n[i]]=i

    return False

print(ans())        