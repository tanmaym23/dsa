class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.childern=children
    
    def __str__(self,level=0) -> str:
        ret="  "*level+str(self.data)+"\n"
        for child in self.childern:
            ret+=child.__str__(level+1)
        return ret
    def addChildren(self,treenode):
        self.childern.append(treenode)

mytree=TreeNode("Drinks",[])
cold=TreeNode("Cold",[])
hot=TreeNode("Hot",[])
mytree.addChildren(cold)
mytree.addChildren(hot)

cola=TreeNode("Cola",[])
fanta=TreeNode("fanta",[])
tea=TreeNode("tea",[])
coffee=TreeNode("coffee",[])
cold.addChildren(cola)
cold.addChildren(fanta)
hot.addChildren(tea)
hot.addChildren(coffee)
print(mytree)

# types of binary trees
# 1.full binary tree -- each node has 0 or 2 childern
# 2.perfect BT -- each node has only 2 childern and at same level
# 3.complete BT -- each node has only 2 childern but not at same level
# 4.balanced BT -- each node is at same level from the root node i.e. at the same level 