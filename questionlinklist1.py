from questionLinkList import LinkList

# q1: remove duplicates
# using temp buffer
def removeDups(ll):
    if ll.head==None:
        return
    else:
        currentNode=ll.head
        visited=set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next=currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode=currentNode.next
        return ll

# without using buffer(higher time complexity but less space complexity)
def removeDups2(llist):
    if llist.head is None:
        return
    else:
        node=llist.head
        while node:
            runner=node
            while runner.next:
                if runner.next.value==node.value:
                    runner.next=runner.next.next
                else:
                    runner=runner.next
            node=node.next
        return llist.head

customL=LinkList()
customL.generate(10,0,99)
print(customL)
removeDups2(customL)
print(customL)