cnt=0
def f(n):
    global cnt
    if cnt==n:
        return cnt
    cnt=cnt+1
    return f(n)
    
print(f(5))    

