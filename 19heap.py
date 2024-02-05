# will impliment binary heap using ARRAY

class Heap:
    def __init__(self,size) -> None:
        self.customlist=(size+1)*[None]
        self.heapSize=0
        self.maxsize=size+1

def peek(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.customlist[1]
    
def size(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapSize
    
def levelorder(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1,rootnode.heapSize+1):
            print(rootnode.customlist[i])

#adjusting tree so it follows property of heap tree --> heapify
def heapifyForInsertion(rootnode,index,heapType): # this index is the index of node we want to adjust
    parentIndex=int(index/2) 
    if index <=1:
        return 
    if heapType=="min":
        if rootnode.customlist[index] < rootnode.customlist[parentIndex]:
           temp=rootnode.customlist[index]
           rootnode.customlist[index] = rootnode.customlist[parentIndex]
           rootnode.customlist[parentIndex] = temp
        heapifyForInsertion(rootnode,parentIndex,heapType)
    elif heapType=="max":
        if rootnode.customlist[index] > rootnode.customlist[parentIndex]:
           temp=rootnode.customlist[index]
           rootnode.customlist[index] = rootnode.customlist[parentIndex]
           rootnode.customlist[parentIndex] = temp
        heapifyForInsertion(rootnode,parentIndex,heapType)
def insert(rootnode,nodeValue,heapType):
    if rootnode.customlist[rootnode.heapSize+1] == rootnode.maxsize:
        return "heap is full"
    rootnode.customlist[rootnode.heapSize+1]=nodeValue
    rootnode.heapSize += 1
    heapifyForInsertion(rootnode,rootnode.heapSize,heapType)
    return "value inserted"

#Note ==> we can only extract root node from heap
def heapifyForExtract(rootnode,index,heapType): # index of currnt node ,i.e., root node
    leftindex=index*2
    rightindex=index*2 +1
    smallestchild=0
    if rootnode.heapSize < leftindex:#no child for current node
        return
    elif rootnode.heapSize == leftindex:# only one node for current node , i.e., left child
        if heapType == "min":
            if rootnode.customlist[index] > rootnode.customlist[leftindex]:
                temp=rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[leftindex]
                rootnode.customlist[leftindex] = temp
        elif heapType == "max":
            if rootnode.customlist[index] < rootnode.customlist[leftindex]:
                temp=rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[rightindex]
                rootnode.customlist[rightindex] = temp
    else:
        if heapType == "min":
            if rootnode.customlist[leftindex] < rootnode.customlist[rightindex]:
                smallestchild = leftindex
            else:
                smallestchild= rightindex
            if rootnode.customlist[index] > rootnode.customlist[smallestchild]:
                temp=rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[smallestchild]
                rootnode.customlist[smallestchild] = temp
        else:
            if rootnode.customlist[leftindex] > rootnode.customlist[rightindex]:
                smallestchild = leftindex
            else:
                smallestchild= rightindex
            if rootnode.customlist[index] < rootnode.customlist[smallestchild]:
                temp=rootnode.customlist[index]
                rootnode.customlist[index] = rootnode.customlist[smallestchild]
                rootnode.customlist[smallestchild] = temp
    heapifyForExtract(rootnode,smallestchild,heapType)
def extract(rootnode,heapType):
    if rootnode.heapSize ==0:
        return
    else:
        extractednode = rootnode.customlist[1]
        rootnode.customlist[1]= rootnode.customlist[rootnode.heapSize]
        rootnode.customlist[rootnode.heapSize]=None
        rootnode.heapSize -=1
        heapifyForExtract(rootnode,1,heapType)
        return " extracted"

def deleteheap(rootnode):
    rootnode.customlist =None
    print("heap deleted")

myheap=Heap(5)
insert(myheap,10,"min")
insert(myheap,40,"min")
insert(myheap,20,"min")
insert(myheap,50,"min")
insert(myheap,30,"min")
levelorder(myheap)
print("------------")
extract(myheap,"min")
levelorder(myheap)
print("------------")
deleteheap(myheap)
levelorder(myheap)