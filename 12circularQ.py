class Cqueue:
    def __init__(self,maxsize) -> None:
        self.maxsize=maxsize
        self.item=maxsize*[None]
        self.start=-1
        self.top=-1

    def __str__(self) -> str:
        value=[str(x) for x in self.item]
        return ' '.join(value)
    
    def isFull(self):
        if self.top + 1== self.start:
            return True
        elif self.start==0 and self.top+1==self.maxsize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top ==-1 and self.start ==-1:
            return True
        else:
            return False
    
    def enqueue(self,value):
        if self.isFull():
            return "queue is full"
        else:
            if self.top+1==self.maxsize:
                self.top=0
            else:
                self.top +=1
                if self.start ==-1:
                    self.start=0
            self.item[self.top]=value
            return "item added"
        
    def dequeue(self):
        if self.isEmpty():
            return "queuenis empty"
        else:
            removed_element=self.item[self.start] # made this to print the removed item
            start=self.start #made this variable to dequeue the element 
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxsize:
                self.start=0
            else:
                self.start=+1
            self.item[start]=None
            return "item removed:",removed_element
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            return self.item[self.start]
        
    def delete(self):
        self.item=self.maxsize*[None]
        self.start=-1
        self.top=-1

myqueue=Cqueue(5)
print(myqueue.isFull())
print(myqueue.isEmpty())
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
print(myqueue)
print("-----------")
myqueue.dequeue()
print(myqueue)
print("-----------")
print(myqueue.peek())
print("-----------")
print(myqueue.delete())