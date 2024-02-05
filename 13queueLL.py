class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
    
class Linklist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class queue:
    def __init__(self) -> None:
        self.linklist=Linklist()
       
    def __str__(self):
        value=[str(x) for x in self.linklist]
        return ' '.join(value)
    
    def isEmpty(self):
        if self.linklist.head==None:
            return True
        else:
            return False
    
    def enqueue(self,value):
        node=Node(value)
        if self.isEmpty():
            self.linklist.head=node
            self.linklist.tail=node
        else:
            self.linklist.tail.next=node
            self.linklist.tail=node

    def dequeue(self):
        removed_node=self.linklist.head #made this to return the removed node 
        if self.isEmpty():
            return "queue is empty"
        else:
            if self.linklist.head==self.linklist.tail:
                self.linklist.head=None
                self.linklist.tail=None 
                return "queue is empty"
            else:
                self.linklist.head=self.linklist.head.next
            return removed_node
        
    def peek(self):
        return self.linklist.head
    
    def delete(self):
        self.linklist.head=None
        self.linklist.tail=None 
    
myqueue=queue()
print(myqueue.isEmpty())
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue)    
print("----------")
print ("removed element:",myqueue.dequeue())
print(myqueue)
print("----------")
print(myqueue.peek())
