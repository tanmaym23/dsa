class node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
 
class linklist:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

ll=linklist()
node1=node(10)
node2=node(20)

ll.head=node1
ll.head.next=node2
ll.tail=node2

print([node.value for node in ll])

