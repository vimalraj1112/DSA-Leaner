"""
num1=int(input("enter the number:"))
num2=int(input("enter the number"))
val=[]
num=0

if num1<num2:
    num=num1
else:
    num=num2    


for i in range(1,num+1):
    if num1%i==0 and num2%i==0:
        val.append(i)

print(max(val))        """

def gcd(x,y):
    for i in range(min(x,y),0,-1):
        if x%i==0 and y%i==0:
            return i


print(gcd(12,6))    


# def gcd(n1,n2): ##Eucladian method

#     while n1!=0 and n2!=0:
#         if n1>n2:
#             n1=n1%n2
#         else:
#             n2=n2%n1

#     return max(n1,n2) 
# print(gcd(12,6))           