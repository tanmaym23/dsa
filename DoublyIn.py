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
            print("NA")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

    def back_traverse(self):
        print()
        if self.head is None:
            print("NA")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data, end=" ")
                a=a.prev

    def ins_beg(self,data):
        print()
        nb=node(data)
        a=self.head
        a.prev=nb
        nb.next=a
        self.head=nb

    def ins_end(self,data):
        print()
        ne=node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a

    def ins_mid(self,position,data):
        print()
        nm=node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nm.next=a.next
        nm.prev=a
        a.next=nm
        a.next.prev=nm
        

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

dll.ins_beg(2)
dll.for_traverse()
dll.back_traverse()

dll.ins_end(25)
dll.for_traverse()

dll.ins_mid(3,7)
dll.for_traverse()