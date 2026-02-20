cnt=0
def fn(n):
    global cnt
    if n==cnt:
        return 
   
    cnt+=1
    print(cnt)
    return fn(n)

fn(5)