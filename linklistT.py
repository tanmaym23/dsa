class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
# node1=Node(7)
# print(node1.data)
# print(node1.reference)

class singly:
    def __init__(self):
        self.head=None

# sll=singly()
# print(sll.head)

    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

n1=Node(5)
sll=singly()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4

sll.traversal()
