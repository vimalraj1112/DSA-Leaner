def ans():
    c=2234

    dic={}
    w='AABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(1,27):
        dic[i]=w[i]

    if c<27:
        
        return dic[c]

    a=''

    while c>0:
        c=c-1
        b=c%26
        c=c//26
        a+=dic[b+1]

    return a[::-1]   



print(ans())
        