def ans():
    class Node:
        def __init__(self,val,next=None):
            self.val=val
            self.next=next
            
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(-4)
    node5=Node(2)

    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node2

    head=node1
    curr=head

    c=set()

    while curr:
        if curr in c:
            return True
        c.add(curr)
        curr=curr.next

    return False

print(ans())    