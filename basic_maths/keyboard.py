def ans():
    b1="qwertyuiop"
    b2="asdfghjkl"
    b3="zxcvbnm"

    words=["Hello","Alaska","Dad","Peace"]

    

    ans=[]

    for i in range(len(words)):
            w=words[i].lower()
            if all(ch in b1 for ch in w):
                ans.append(words[i])
            elif all(ch in b2 for ch in w):
                ans.append(words[i])
            elif all(ch in b3 for ch in w):
                ans.append(words[i])        

    return ans   

print(ans())      