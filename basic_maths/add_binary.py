def ans():
    a='11'
    b='1'

    ans=[]

    dec=int(a,2)+int(b,2)   
    
    while dec>0:
        ans.append(str(dec%2))
        dec=dec//2
        
    return ''.join(ans[::-1])
print(ans())
