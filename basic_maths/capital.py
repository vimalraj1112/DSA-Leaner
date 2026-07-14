def ans():
    w = "FlaG"

    b=0

    if w in w.upper():
        return True
    
    
    for i in range(1,len(w)):
        if w[0] in w[0].upper() and w[i] in w[i].lower():
            continue
        else:
            b+=1

    if b>0:
        return False
    return True        

print(ans())
        
