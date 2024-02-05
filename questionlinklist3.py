# partition of link list
from questionLinkList import LinkList

def partition(ll,n):
    currentnode=ll.head
    ll.tail=ll.head

    while currentnode:
        nextnode=currentnode.next
        currentnode.next=None
        if currentnode.value < n:
            currentnode.next=ll.head
            ll.head=currentnode
        else:
            ll.tail.next=currentnode
            ll.tail=currentnode
        currentnode=nextnode
    
    if ll.tail.next is not None:
        ll.tail.next=None

customL=LinkList()
customL.generate(10,0,99)
print(customL)
partition(customL,50)
print(customL)