# BST using linklist
import QUEUE as queue
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.leftchild=None
        self.rightchild=None

def insertion(rootnode, nodevalue):
    if rootnode.data==None:
            rootnode.data=nodevalue
    elif nodevalue<=rootnode.data:
        if rootnode.leftchild is None:
            rootnode.leftchild=node(nodevalue)
        else:
            insertion(rootnode.leftchild,nodevalue)
    else:
        if rootnode.rightchild is None:
            rootnode.rightchild=node(nodevalue)
        else:
            insertion(rootnode.rightchild,nodevalue)

def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)

def search(rootnode,nodevalue):
    if rootnode.data==nodevalue:
        print("element found") 
    elif nodevalue<rootnode.data:
        if rootnode.leftchild.data == nodevalue:
            print("element found")
        else:
            search(rootnode.leftchild,nodevalue)
    else :
        if rootnode.rightchild.data == nodevalue:
            print("element found")
        else:
            search(rootnode.rightchild,nodevalue)

# def levelorder(rootnode):
#     if not rootnode:
#         return
#     else:
#         customqueue=queue.Queue()
#         customqueue.enqueue(rootnode)
#         while not(customqueue.isEmpty()):
#             root=customqueue.dequeue
#             print(root.value.data)
#             if rootnode.value.leftchild is not None:
#                 customqueue.enqueue(root.value.leftchild)
#             if rootnode.value.rightchild is not None:
#                 customqueue.enqueue(root.value.rightchild)
                  

myBST=node(70)
insertion(myBST,50)
insertion(myBST,90)
insertion(myBST,30)
insertion(myBST,60)
insertion(myBST,80)
insertion(myBST,100)
insertion(myBST,20)
insertion(myBST,40)
print(myBST.data)#value of root node
print(myBST.rightchild.data)
print(myBST.leftchild.data)
# print(myBST.leftchild.rightchild.data)
# print(myBST.leftchild.rightchild.leftchild.data)
print("----------")
# preorder(myBST)
# levelorder(myBST)

search(myBST,65)