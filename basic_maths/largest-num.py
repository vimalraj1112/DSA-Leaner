import array as arr

def largest_num():

    arrray=arr.array('i',[10,2,3,4,5,1])
    lar=0

    for i in range(len(arrray)):
        if lar<arrray[i]:
            lar=arrray[i]

    return lar        

print(largest_num())

