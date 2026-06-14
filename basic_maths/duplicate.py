def ans():
    nums=[1,1,2,2,3,3,4,5]
    
    n=len(nums)

    count=0
    

    for i in range(1,n):
        if nums[count] != nums[i]:
            count+=1
            nums[count]=nums[i]
            




    return count+1
           



print(ans())        