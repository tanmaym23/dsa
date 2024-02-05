class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None

    def for_traverse(self):
        if self.head is None:
            print("N.A.")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ") 
                a=a.next

    def back_traverse(self):
        print()
        if self.head is None:
            print("N.A.")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data, end=" ")
                a=a.prev

n1=node(5)
dll=DLL()
dll.head=n1
n2=node(10)
n2.prev=n1
n1.next=n2
n3=node(15)
n3.prev=n2
n2.next=n3
n4=node(20)
n4.prev=n3
n3.next=n4
dll.for_traverse()
dll.back_traverse()
