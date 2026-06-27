from collections import Counter

def ans():
    n1=[1,2,1,1]
    n2=[2,2]

    ans=[]
    c=Counter(n1)
    
    for i in n2:
        if i in c and c[i]>0:
            ans.append(i)
            c[i]-=1
    return ans
print(ans())    