class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

node1=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)    

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

head=node1
prev=None
curr=head

while curr:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next

head=prev
curr=head

while curr:
    print(curr.val)
    curr=curr.next
    




   