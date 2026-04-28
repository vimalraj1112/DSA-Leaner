def ans():
    x=['vimal','raj','vi']

    lst=[]
    y='i'
    c=0

    for i in range(len(x)):
        
        if x[c][i]==y:
            lst.append(c)
            c+=1
            break
        else:
            c+=1

    return lst

print(ans())      