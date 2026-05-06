class Node():

    def __init__(self,data):
        self.data=data
        self.next=None

class MyLinkedList:


    def __init__(self):
        self.head=None
        

    def get(self, index: int) -> int:
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
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        if not self.head:
            self.head= new_node

        new_node.next=self.head
        self.head=new_node
        

    def addAtTail(self, val: int) -> None:
        new_node=Node(val) 

        if not self.head:
            self.head=new_node
            return 

        current=self.head

        while current.next:
            current=current.next

        current.next=new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node=Node(val)
        
        
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
        

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        
        if index==0:
            self.head=self.head.next  
        
        current=self.head
        i=0
        while current:
            if index-1==i:
                if current.next:

                    current.next=current.next.next
            current=current.next
            i+=1 