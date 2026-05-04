class Node():

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None

    def add_at_tail(self,data):
        new_node=Node(data) 

        if not self.head:
            self.head=new_node
            return 

        current=self.head

        while current.next:
            current=current.next

        current.next=new_node

    def add_at_head(self,data):
        new_node=Node(data)
        if not self.head:
            self.head= new_node

        new_node.next=self.head
        self.head=new_node


    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
linkedlist=linkedlist()
linkedlist.add_at_tail(1) 
linkedlist.add_at_tail(2)
linkedlist.add_at_tail(3)
linkedlist.add_at_head(0)


linkedlist.display()     