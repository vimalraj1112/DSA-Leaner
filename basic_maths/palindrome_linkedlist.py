def ans():
    class Node:
        def __init__(self,val,next=None):
            self.val=val
            self.next=next

    node1=Node(1)        
    node2=Node(2)        
    node3=Node(2)        
    node4=Node(3)   

    node1.next=node2
    node2.next=node3
    node3.next=node4

    head=node1

    s=head
    f=head

    while f and f.next:
        s=s.next
        f=f.next.next

    prev=None

    while s:
        nxt=s.next
        s.next=prev
        prev=s
        s=nxt

    left=head
    right=prev

    while right:
        if left.val != right.val:
            return False
        left=left.next
        right=right.next    

    return True

print(ans())