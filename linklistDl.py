class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def traverse(self):
        if self.head is None:
            print("N.A.")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

    def del_beg(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None

    def del_end(self):
        print()
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None

    def del_mid(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None

n1=node(5)
sll= LL()
sll.head=n1
n2=node(10)
n1.next=n2
n3=node(15)
n2.next=n3
n4=node(20)
n3.next=n4
n5=node(25)
n4.next=n5
n6=node(30)
n5.next=n6
sll.traverse()

sll.del_beg()
sll.traverse() 

sll.del_end()
sll.traverse() 

sll.del_mid(2)
sll.traverse()