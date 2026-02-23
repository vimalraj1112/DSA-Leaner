cnt=0
v=0
def sum(n):
    global v
    global cnt
    if n==0:
        return cnt
    n-=1
    v+=1
    cnt=cnt+v 
    
    return sum(n)
    


print(sum(5))