def ans():
    n=[2,1,2,3,5,1,5]

    ans=0

    for i in n:
        ans^=i

    return ans

print(ans())        