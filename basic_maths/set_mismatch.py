def ans():
    nums=[1,2,2,4]
    d={}

    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1


    a=[]

    for i in range(1,len(nums)+1):
        if i in d:
            if d[i]>1:
                a.append(i)
    for i in range(1,len(nums)+1):
        if i not in d:
            a.append(i)
    return a

print(ans())