class Node():

    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None

    def addAtTail(self,data):
        new_node=Node(data) 

        if not self.head:
            self.head=new_node
            return 

        current=self.head

        while current.next:
            current=current.next

        current.next=new_node

    def addAtHead(self,data):
        new_node=Node(data)
        if not self.head:
            self.head= new_node

        new_node.next=self.head
        self.head=new_node

    def get(self,index):
        if not self.head:
            return -1
        i=0
        current=self.head
        while current:

            if i==index:
                return current.data
            current=current.next
            i+=1
        return -1
    
    def addAtIndex(self,index,data):
        new_node=Node(data)
        if not self.head:
            if index==0:
                self.head=new_node
            return
        
        if index==0:
            if self.head:
                new_node.next=self.head
                self.head=new_node

            else:
                self.head=new_node    
        
        current=self.head
        i=0
        while current:
            if index==i+1:
                new_node.next=current.next
                current.next=new_node
            current=current.next    
            i+=1    


                
            
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next

linkedlist=linkedlist()
linkedlist.addAtTail(1) 
linkedlist.addAtTail(2)
linkedlist.addAtTail(3)
linkedlist.addAtHead(0)
print(linkedlist.get(7))
print(linkedlist.addAtIndex(0,'new'))

linkedlist.display()     