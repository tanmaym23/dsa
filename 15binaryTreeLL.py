class TreeNode():
    def __init__(self,data) -> None:
        self.data=data
        self.leftchild=None
        self.rightchild=None
    
mytree=TreeNode("Drinks")
hot=TreeNode("hot drinks")
cold=TreeNode("cold drinks")
coffee=TreeNode("coffee")
tea=TreeNode("tea")

mytree.leftchild=hot
mytree.rightchild=cold

hot.leftchild=coffee
hot.rightchild=tea

#  PRE ORDER TRAVERSAL= ROOT NODE --> LEFT SUBTREE --> RIGHT SUBTREE
def preorder(rootnode):
    if not rootnode:
        return 
    print (rootnode.data) 
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)

preorder(mytree)

#  IN ORDER TRAVERSAL= LEFT SUBTREE --> ROOT NODE ==> RIGHT SUBTREE
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)

print("---------------")
inorder(mytree)

#  POST ORDER TRAVERSAL = LEFT SUBTREE --> RIGHT SUBTREE --> ROOT NODE 
def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)

print("---------------")
postorder(mytree)
print("***************")

# LEVEL ORDER TRAVERSAL = LEVEL1--> LVL2 --> LVL3--> AND SO ON
import QUEUE as queue

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        mqueue=queue.Queue()
        mqueue.enqueue(rootnode)
        while not (mqueue.isEmpty()):
            root=mqueue.dequeue()
            print(root.value.data)

            if (root.value.leftchild is not None):
                mqueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                mqueue.enqueue(root.value.rightchild)


levelorder(mytree)
