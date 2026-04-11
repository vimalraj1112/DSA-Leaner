n=int(input("enter the number:"))
ans=[]

for i in range(1,n//2+1):
    if n%i==0:
        ans.append(i)
ans.append(n)
print(ans)        

# from math import *
# n=36

# ans=[]

# for i in range(1,int(sqrt(n))+1):
#     if n%i==0:
#         ans.append(i)
#         if n//i != i:
#             ans.append(n//i)

# print(sorted(ans))              