a=[1,2,3,4,4,3,3,1,5,6,7,6]

dic={}

for i in a:
    if dic.get(i):
        dic[i]+=1
    else:
        dic[i]=1

print(dic)        

