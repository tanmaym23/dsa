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

    def insertion(self,value,location):
        newnode=node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            # elif location==1:
            #     newnode.next=None
            #     self.tail.next=newnode
            #     self.tail=newnode
            else:
                temp=self.head
                index=0
                while index<location-1:
                    temp=temp.next 
                    index += 1
                nextnode=temp.next
                temp.next=newnode
                newnode.next=nextnode

    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else: 
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next

    def search(self,value):
        if self.head is None:
            return"link list doesnt exist"
        else:
            node=self.head
            while node is not None:
                if node.value==value:
                    return node.value
                node=node.next
            return "value doesnt exist"

ll=linklist()
ll.insertion(10,1)
ll.insertion(20,1)
ll.insertion(30,1)

ll.insertion(5,0)

ll.insertion(40,4)

print([node.value for node in ll])
ll.traversal()
print(ll.search(30))