class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

    def insertion_beg(self, data):
        print()
        nb=node(data)
        nb.next=self.head
        self.head=nb

    def insertion_end(self,data):
        print()
        ne=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne

    def insertion_mid(self,position,data):
        print()
        nib=node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.next=a.next
        a.next=nib        

n1=node(5)
sll=LL()
sll.head=n1
n2=node(10)
n1.next=n2
n3=node(15)
n2.next=n3
n4=node(20)
n3.next=n4
sll.traversal()

sll.insertion_beg(2)
sll.traversal()

sll.insertion_end(25)
sll.traversal()

sll.insertion_mid(3,7)
sll.traversal()