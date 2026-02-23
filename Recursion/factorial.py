ans=1
def fac(i,n):
    global ans
    if i>n:
        return ans
    ans=ans*i
    i+=1
    return fac(i,n)

print(fac(1,5))
