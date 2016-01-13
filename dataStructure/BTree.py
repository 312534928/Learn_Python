class TreeNode(object):  # 树节点对象
    def __init__(self, data=0, left=0, right=0):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=0):
        self.root = root

    def is_empty(self):
        if self.root is 0:
            return True
        else:
            return False

    def preOrder(self, treenode):  # 先序遍历
        if treenode is 0:
            return
        print(treenode.data)
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)

    def inOrder(self, treenode):  # 中序遍历
        if treenode is 0:
            return
        self.preOrder(treenode.left)
        print(treenode.data)
        self.preOrder(treenode.right)

    def postOrder(self, treenode):  # 后序遍历
        if treenode is 0:
            return
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)
        print(treenode.data)


n1=TreeNode(1)
n2=TreeNode(2,n1,0)
n3=TreeNode(3)
n4=TreeNode(4)
n5=TreeNode(5,n3,n4)
n6=TreeNode(6,n2,n5)
n7=TreeNode(7,n6,0)
n8=TreeNode(8)
root=TreeNode("root",n7,n8)

bt=BTree(root)
print("preOrder:")
bt.preOrder(bt.root)
print("inOrder:")
bt.inOrder(bt.root)
print("postOrder:")
bt.postOrder(bt.root)