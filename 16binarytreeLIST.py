# it is prefered to use PYTHON LIST for binary tree than linklist
# PYTHON LIST is not space efficient

class BinaryTree:
    def __init__(self,size):
        self.customlist=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size

    def insertion(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return " tree is full"
        else:
            self.customlist[self.lastUsedIndex+1]=value
            self.lastUsedIndex +=1
            return "success"
        # return self.customlist
    
    def search(self,nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i]==nodevalue:
                print("found",nodevalue ,"at" , self.lastUsedIndex+1 , "index")
                return "element found"
        return "not found"
    
    def preorder(self,index):
        if index>self.lastUsedIndex:
            return 
        print(self.customlist[index])
        self.preorder(index*2)
        self.preorder(index*2 +1)

    def inorder(self,index):
        if index>self.lastUsedIndex:
            return 
        self.inorder(index*2)
        print(self.customlist[index])
        self.inorder(index*2 +1)

    def postorder(self,index):
        if index>self.lastUsedIndex:
            return 
        self.postorder(index*2)
        self.postorder(index*2 +1)
        print(self.customlist[index])

    def levelorder(self,index):
        for i in range (index,self.lastUsedIndex+1):
            print(self.customlist[i])

    def deletenode(self,value):
        if self.lastUsedIndex==0:
            return "no node in tree"
        for i in range(1,self.lastUsedIndex):
            if self.customlist[i]==value:
                self.customlist[i]=self.customlist[self.lastUsedIndex]
                self.customlist[self.lastUsedIndex]=None
                self.lastUsedIndex -=1
                return "node deleted"

    def deletetree(self):
        self.customlist = None
        return "tree deleted"
    
myBT=BinaryTree(8)
print(myBT.insertion("drinks"))
print(myBT.insertion("hot"))
print(myBT.insertion("cold"))
print(myBT.insertion("tea"))
print(myBT.insertion("coffee"))
print("----------")
print(myBT.search("cold"))
print("----------")
myBT.preorder(1)
print("----------")
myBT.inorder(1)
print("----------")
myBT.postorder(1)
print("----------")
myBT.levelorder(1)
print("----------")
myBT.deletenode("tea")
myBT.levelorder(1)