# Stack using liST WITHOUT limit

class Stack:
    def __init__(self):
        self.list=[1,2,3,4] 

    def __str__(self):
        value=self.list.reverse()
        value=[str(x) for x in self.list]
        return '\n'.join(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)
        return "element inserted"
    
    def pop(self):
        if self.list==[]:
            return "list is empty"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "list is empty"
        else :
            return self.list[len(self.list)-1]
 
    def delStack(self):
        self.list=None
    
mystack=Stack()
print(mystack)

# print(mystack.isEmpty())

mystack.push(5)
print(mystack)
mystack.pop()
print(mystack)

# print("top element:" ,mystack.peek())
# mystack.delStack()
# print(mystack)


           
