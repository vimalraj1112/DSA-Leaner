def ans():

    nums=[-1,0,1,2,-1,-4]
        
    ans=[]
    nums.sort()

    for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            while right>left:

                s=nums[i]+nums[left]+nums[right]
                a=[nums[i],nums[left],nums[right]]
                if s==0:
                    ans.append(a)
                    left+=1
                    right-=1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1    
                elif s<0:
                    left+=1
                elif s>0:
                    right-=1    


            
    return ans   
print(ans())             
