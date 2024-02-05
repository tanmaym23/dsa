# push will add new element as head everytime and pop will deleted that newly added head.
# older elements will automatically be moved to next indexes  
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linklist:
    def __init__(self):
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next


class stack:
    def __init__(self):
        self.linklist=linklist() 

    def __str__(self):
        value=[str(x.value) for x in self.linklist]
        return '\n'.join(value)
    
    def isEmpty(self):
        if self.linklist.head==None:
            return True
        else:
            return False
        
    def push(self,value):
        node=Node(value)
        node.next=self.linklist.head
        self.linklist.head=node

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            nodeValue=self.linklist.head.value
            self.linklist.head=self.linklist.head.next
            return nodeValue
        
    def peep(self):
        if self.isEmpty():
            return " stack is empty"
        else:
            nodeValue=self.linklist.head.value
            return nodeValue
    
    def delete(self):
        self.linklist.head=None


mystack=stack()
# print(mystack.isEmpty()) 
mystack.push(10)
mystack.push(20)
mystack.push(30)
print(mystack)
print("----------")
mystack.pop()
print( mystack)
print("----------")
print(mystack.peep())
# mystack.delete()