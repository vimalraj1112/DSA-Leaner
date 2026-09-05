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
        
# def ans():
#     n=[3,9,2,1,7]
#     k=3

#     d={}

#     for i in range(len(n)-k+1):
#         b=n[i:i+k]
#         for j in b:
#             if j in d:
#                 d[j]+=1
#             else:
#                 d[j]=1

#     ans=-1
#     for j in d:
#         if d[j]==1:
#             ans=max(ans,j)

#     return ans        



                            

# print(ans())            

# def ans():
#     n = [2,3,4,3,4] 
#     a=0
#     b=0
#     ans=0

#     for i in range(1,len(n)):
#         diff=n[i]-n[i-1]
#         if diff==1:
#             a+=1
#         else:
#             ans=max(ans,a)
#             a=2
#         b=1
#         if diff==-1:
#             if b==1:
#                 a+=1
#             b=1
#         else:
#             ans=max(ans,a)
#             a=0    
                
#     ans=max(ans,a)
#     if ans==0:
#         return -1
#     return ans
# print(ans())      

# def ans():
#     n=23
#     a=n
#     x=0
#     y=1
#     for i in range(len(str(n))):
#         x+=a%10
#         y*=a%10
#         a=a//10
#     print(x,y)
#     if n%(x+y)==0:
#         return True
#     return False 
# print(ans())
            
def ans():
    n=[5,0,1,4]

    k=3

    
    for i in range(len(n)):
        a=n[0:i+1]
        b=n[i:len(n)]
        print(a,b)

        ans=max(a)-min(b)
        if k>=ans:
            return i
    return -1    
        

               
print(ans())    
