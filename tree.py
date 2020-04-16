#Basic Node definition. Each Node contains a Value, a left child, and a right child
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

#insert Value into the appropiate spot in the tree
def insert(root, node):

    if root is None:
        root=node
    elif root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)


def search(root, value):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == value:
        return root
    # Key is greater than root's key
    if root.val < value:
        return search(root.right, value)
    # Key is smaller than root's key
    return search(root.left, value)

def inorder_traversal(root):
    #finish code to print all values with an inorder traversal
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)
def preorder_traversal(root):
    if root is not None:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)
def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)

bst = Node(5)
insert(bst,Node(2))
insert(bst,Node(7))
insert(bst,Node(10))
insert(bst,Node(4))
insert(bst,Node(1))

inorder_traversal(bst)
preorder_traversal(bst)
postorder_traversal(bst)


val=10
if search (bst,val):
    print ("True")
else:
    print("False")






