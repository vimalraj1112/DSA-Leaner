# def ans():

#     nums=[1,2,3,2,5]
#     ans=nums[0]

#     for i in range(1,len(nums)):
#         if nums[i]==nums[i-1]+1:
#             ans+=nums[i]
#         else:
#             break

#     while ans:
#         if ans in nums:
#             ans+=1
#         else:
#             return ans            
            
    

# print(ans())

# def ans():
#     v=[1,5,10,50,100,500,1000]
#     s='IVXLCDM'
#     num = 3749
#     d={}

#     for i in range(len(v)):
#         d[v[i]]=s[i]
#     print(len(str(num))+1)
#     return d
# print(ans())    

# def ans():
#     n=15

#     ans=[]

#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             ans.append('FizzBuzz')
#         if i%3==0:
#             ans.append('Fizz')
#         if i%5==0:
#             ans.append('Buzz')
#         if i%3!=0 and i%5!=0:
#             ans.append(str(i))

#     return ans

# print(ans())        

# def ans():
#     s = "Hello, my name is John"

#     a=[]

#     x=s.split()
#     print(len(x))

# print(ans())

# def ans():
#     w='aba'
#     a=0

#     for i in range(len(w)):
#         for j in range(i+1):
#             print(j)
#             if w[j] in 'aeiou':
#                 a+=1
#     return a 
# print(ans())   

# def ans():

#     date = "2019-02-10"

#     y=''
#     day=''
#     m=''

#     d=[0,31,59,90,120,151,181,212,243,273,304,334]

#     y+=date[0]
#     y+=date[1]
#     y+=date[2]
#     y+=date[3]
#     m+=date[5]
#     m+=date[6]
#     day+=date[8]
#     day+=date[9]

#     x=d[int(m)-1]
#     x+=int(day)

#     if int(y)%400==0:
#         return x+1
#     return x


    

# print(ans())    
        
def ans():
    n=[3,9,2,1,7]
    k=3

    d={}

    for i in range(len(n)-k+1):
        b=n[i:i+k]
        for j in b:
            if j in d:
                d[j]+=1
            else:
                d[j]=1

    ans=-1
    for j in d:
        if d[j]==1:
            ans=max(ans,j)

    return ans        



                            

print(ans())            

            