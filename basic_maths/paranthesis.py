def ans():
    
    s="([)]"

    st=[]
    d={'(':')','{':'}','[':']'}

    if len(s)%2!=0:
        return False

    for i in s:
        if i in d:
            st.append(i)
        else:
            if st==[]:
                return False
            else:
                if d[st[-1]]==i:
                    st.pop()
                else:
                    return False

    if st==[]:
        return True
    return False                

           

       

print(ans())