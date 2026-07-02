def ans():
    nums=[4,3,2,7,8,2,3,1]
    ans=[]
        
    for i in range(len(nums)):
            val=abs(nums[i])
            ind=val-1
            if nums[ind]>0: 
                nums[ind]=-nums[ind]
    for i in range(len(nums)):        
            if nums[i]>0:
                ans.append(i+1)

    return ans

print(ans())