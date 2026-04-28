def ans():
    x='hello iam vimal '
    count=0

    for i in range(len(x)-1,0,-1):
        if x[i]!=' ':
            count+=1
        elif count != 0:
            break

    return count

print(ans())        