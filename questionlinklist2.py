# q2: remove nth to last (nth element from last)
# eg- if n=3, we need to return 3rd last element
from questionLinkList import LinkList

def nthToLast(ll,n):
    pointer1=ll.head
    pointer2=ll.head
    for i in range(n):
        if pointer2 is None:
            return
        pointer2=pointer2.next

    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next

    return pointer1

customL=LinkList()
customL.generate(10,0,99)
print(customL)

print(nthToLast(customL,4))