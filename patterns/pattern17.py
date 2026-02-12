def diffi():
    n=4
    v=65

    for i in range(n):
        for j in range(1,n-i):
            print("_",end=" ")

        for j in range(i+1):
            x=chr(v)
            print(x,end=" ")
            v=v+1
            
        v=v-1
        for j in range(i):
            v=v-1

            x=chr(v)
            print(x,end=" ")
            

                    
            
            
                
        print()
        v=65

diffi()            
