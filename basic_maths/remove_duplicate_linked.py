def ans():
    class Node:
        def __init__(self,val,next=None):
            self.val=val
            self.next=next

    node1=Node(1)
    node2=Node(1)
    node3=Node(2)

    node1.next=node2
    node2.next=node3

    head=node1
    curr=head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next=curr.next.next

        else:
            curr=curr.next

    return head    

print(ans())                