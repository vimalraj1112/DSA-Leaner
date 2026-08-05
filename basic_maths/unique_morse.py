def ans():
    h=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    w='abcdefghijklmnopqrstuvwxyz'

    dic={}

    wd=["gin","zen","gig","msg"]

    d=[]

    for i in range(len(w)):
        dic[w[i]]=h[i]

    for i in range(len(wd)):
        a=''
        for j in wd[i]:
        
            if j in dic:
                a+=dic[j]
        d.append(a)  
        a=''     
                
    
    return len(set(d))            
print(ans())
        
