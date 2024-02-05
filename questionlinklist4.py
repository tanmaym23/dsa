# q4:sum linklist

from questionLinkList import LinkList

def sum(llA,llB):
    n1=llA.head
    n2=llB.head
    carry=0

    ll=LinkList()

    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.add(int(result%10))
        carry=result/10
    return ll

llA=LinkList()
llA.add(4)
llA.add(5)
llA.add(6)

llB=LinkList()
llB.add(4)
llB.add(3)
llB.add(2)

print(llA)
print(llB)
print(sum(llA,llB))



