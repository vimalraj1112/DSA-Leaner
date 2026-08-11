def ans():

    nums=[1,2,3,2,5]
    ans=nums[0]

    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]+1:
            ans+=nums[i]
        else:
            break

    while ans:
        if ans in nums:
            ans+=1
        else:
            return ans            
            
    

print(ans())