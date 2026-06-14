def ans():
    n=[1,2,3]

    s=[[]]

    for i in n:
        new=[]
        for sub in s:
            new.append(sub+[i])

        s.extend(new)

    return s

print(ans())        