def ans():
    x='abcd1234abcd55'
    max=-1
    smax=-1



    for i in range(len(x)):
        if x[i].isdigit():
            if int(x[i])>max:
                smax=max
                max=int(x[i])
            elif smax<int(x[i]) and int(x[i])!=max:
                smax=int(x[i])

    return smax               

    
    
    

    

    


print(ans())    