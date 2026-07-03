def ans():

    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

    dic={}

    for i in range(len(list2)):
        dic[list2[i]]=i

    ans=[]
    a=float('inf')

    for i in range(len(list1)) :
        if list1[i] in list2:
            j=dic[list1[i]]
            b=i + j
            if a>b:
                a=b
                ans=[list1[i]]
            elif a==b:
                ans.append(list1[i])  

    return ans           

print(ans())