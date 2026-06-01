def ans():
    cost=[6,5,7,9,2,2]
    cost.sort(reverse=True)
    ans=0

    for i in range(len(cost)):
        if i%3 != 2:
            ans+=cost[i]
    return ans

print(ans())        