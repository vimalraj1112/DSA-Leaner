
class Node:
    def __init__(self,val,next=None):
            self.val=val
            self.next=next

node1=Node(1)        
node2=Node(2)        
node3=Node(3)        
node4=Node(4)        
            
node1.next=node2
node2.next=node3
node3.next=node4

v=2
head=node1
curr=head
prev=None

while curr:
        if curr.val == v:
        
            prev.next=curr.next
            break
        prev=curr    
        curr=curr.next

curr=head
while curr:
    print(curr.val)
    curr=curr.next        

    


    



