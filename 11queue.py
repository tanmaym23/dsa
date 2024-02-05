# PREFORMES BETTER THAN STACK
class Queue:
    def __init__(self) -> None:
        self.item=[]

    def __str__(self) -> str:
        value=[str(x) for x in self.item] 
        return ' '.join(value)
    
    def isempty(self):
        if self.item ==[]:
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.item.append(value)
        return "item inserted"
    
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
            self.item.pop(0)

    def peek(self):
        if self.isempty():
            return "queue is empty"
        else:
            return self.item[0]

myqueue=Queue()
print(myqueue.isempty())
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
print(myqueue)
print("----------")
myqueue.dequeue()
print(myqueue)
print("----------")
print(myqueue.peek())
