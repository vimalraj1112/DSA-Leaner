def short():
    list=['hello','i','am','hello']
    start=1
    target='hello'
    n=len(list)
    ans=[]

    for i in range(start,n*2):
        index=((i) % n)
        if list[index]==target:
            ans.append(index-start)
    print(ans)
    return(min(ans))        

print(short())      


        