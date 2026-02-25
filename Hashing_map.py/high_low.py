from array import *
from collections import *

a=array('i',[10,5,10,15,10,5])

freq={}
b=[]
max_key=0
max_val=0
min_key=0
min_val=100

for i in a:
    if freq.get(i):
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]<min_val:
        min_val=freq[i]
        min_key=i

    if freq[i]>max_val:
        max_val=freq[i]
        max_key=i

print(min_key) 
print(max_key)            

           

        



    

      