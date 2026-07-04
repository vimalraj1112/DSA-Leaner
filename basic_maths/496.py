def ans():
    n1 = [4,1,2]
    n2 = [1,3,4,2]

    ans=[]

    for i in range(len(n1)):
        if n1[i] in n2:
            ind=n2.index(n1[i])
            if ind==len(n2)-1:
                ans.append(-1)
                continue
            found=False    

            for j in range(ind+1,len(n2)-1):
                if n1[i]<n2[j]:
                    ans.append(n2[j])
                    found=True
                    break

            if not found:
                ans.append(-1)

    return ans

print(ans())                