def ans():
        nums=[0,1,2,4,5,7]
        ans=[]
        if len(nums)==0:
            return []

        start=nums[0]    
        
        for i in range(len(nums)-1):
            
            if nums[i]+1 != nums[i+1]:
                
                if start==nums[i]:
                    
                    ans.append(str(start))
                else:
                    ans.append(str(start)+'->'+str(nums[i]))
                start=nums[i+1]
        if start == nums[-1]:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(nums[-1]))

        return ans             
            
print(ans())            
                    