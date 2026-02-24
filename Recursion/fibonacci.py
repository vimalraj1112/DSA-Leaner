n=5
def fib(a,b):
    global n
    if n==0:
        return b
    n-=1
    return fib(b,a+b)
print(fib(0,1))