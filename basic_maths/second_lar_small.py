import array as arr

def ans():
    array=arr.array('i',[1,2,5,7,7,4])

    sett=set(array)

    ans=[]

    for i in range(len(sett)):
        ans.append(array[i])
        
    ans2=sorted(ans) 
    
    set1=set(ans)
    set2=list(set1)
    


    


    print(set2[1])
    print(set2[len(set2)-2])
    

ans()        