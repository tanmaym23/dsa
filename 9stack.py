# stack using list WITH limit

class stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list=[]

    def __str__(self):
        value=self.list.reverse()
        value=[str(x) for x in self.list]
        return '\n'.join(value)
    
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list)==self.maxsize:
            return True
        else: 
            return False
        
    def push(self,value):
        if self.isFull():
            return "stack is full"
        else:
            return self.list.append(value)
        
    def pop(self):
        if self.isempty():
            return "stack is empty"
        else:
            self.list.pop()
        
mystack=stack(4)        
print(mystack.isempty())
print(mystack.isFull())

mystack.push(1)
mystack.push(2)
mystack.push(3)    
print(mystack)