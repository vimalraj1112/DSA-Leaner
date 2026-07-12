def ans():
    s = "I speak Goat Latin"
    
    a=s.split()
    ans=[]
    m='maa'
    

    for i in a:
        if i[0].lower() in 'aeiou':
            ans.append(i+m)
            m+='a'

        else:
            y=i[1:]
            ans.append(y+i[0]+m)
            m+='a'
    return ' '.join(ans)
    
print(ans())