def ans():
    n=[4,3,2,7,8,2,3,1]

    x=set()
    y=[]
    
    for i in n:
        if i not in x:
            x.add(i)
        else:
            y.append(i)
        
                

        
            

    return y
print(ans())        