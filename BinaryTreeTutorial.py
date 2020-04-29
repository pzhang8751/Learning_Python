

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # create root
root = Node(1)
'following is the tree after above statement'
root.left = Node(2)
root.right = Node(3)
'2 and 3 become left and right children of 1'
root.left.left = Node(4)
'4 becomes left child of 2'

# Binary Tree Properties
'L <= 2l - 1[From Point 1] \
l =   ? Log2L ? + 1 \
where l is the minimum number of levels'

'L = T + 1 \
Where L = Number of leaf nodes \
T = Number of internal nodes with two children'

# Types of Binary Trees
'Full binary tree = 0 or 2 children on each node \
Leaf nodes = internal nodes + 1'

'Perfect binary tree = 2 children each node and same level nodes \
Tree height = 2^h - 1 node'

'degenerate tree = only one child per node'

# Handshaking Lemma + Interesting Tree Properties
'L = (k - 1)*I + 1 \
Where L = Number of leaf nodes \
I = Number of internal nodes'

"Sum of all degrees = 2 * (Sum of Edges)' \
Sum of degrees of leaves + Sum of degrees for Internal Node except root + Root's degree = 2 * (No. of nodes - 1) \
Putting values of above terms, \
L + (I - 1) * (k + 1) + k = 2 * (L + I - 1) \
L + k * I - k + I - 1 + k = 2 * L + 2I - 2 \
L + K * I + I - 1 = 2 * L + 2 * I - 2 \
K * I + 1 - I = L \
(K - 1) * I + 1 = L"

# Enumeration of Binary Trees
"A Binary Tree is labeled if every node is assigned a label and \
a Binary Tree is unlabeled if nodes are not assigned any label."

"N = node \
For n  = 1, there is only one tree \
For n  = 2, there are two trees \
For n  = 3, there are five trees"

"For example, let T(n) be count for n nodes. \
T(0) = 1  [There is only 1 empty tree] \
T(1) = 1 \
T(2) = 2 \
T(3) =  T(0)*T(2) + T(1)*T(1) + T(2)*T(0) = 1*2 + 1*1 + 2*1 = 5 \
T(4) =  T(0)*T(3) + T(1)*T(2) + T(2)*T(1) + T(3)*T(0) \
     =  1*5 + 1*2 + 2*1 + 5*1 \
     =  14 \
T(n) = (2n)! / (n + 1)!n! \
Number of Labeled Tees = (Number of unlabeled trees) * n! \
                       = [(2n)! / (n+1)!n!]  × n!"

# Insertion in Binary Tree
# Python program to insert element in binary tree


class newNode():
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


""" Inorder traversal of a binary tree"""


def inorder(temp):
    if (not temp):
        return

    inorder(temp.left)
    print(temp.key, end=" ")
    inorder(temp.right)


"""function to insert element in binary tree """


def insert(temp, key):
    q = []
    q.append(temp)

    # Do level order traversal until we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

        # Driver code


if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)

    print("Inorder traversal before insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after insertion:", end=" ")
    inorder(root)

# Deleting Node in Binary Tree
# Python3 program to illustrate deletion in a Binary Tree

# class to create a node with data, left child and right child.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Inorder traversal of a binary tree
def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


# function to delete the given deepest node (d_node) in binary tree
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

            # function to delete element in binary tree


def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root


# Driver code
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)

# BFS and DSF
'BFS = root, 1st layer, 2nd layer, etc.'
def DFS():
    class Binary_Tree():
        def __init__(self, key):
            self.val = key
            self.left = None
            self.right = None
            self.parent = None

    def inorder(root):
        if root:
            inorder(root.left)

            print(root.val)
            inorder(root.right)

    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.val)

    def preorder(root):

        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)

    hi = Binary_Tree(1)
    hi.left = Binary_Tree(2)
    hi.right = Binary_Tree(3)
    hi.left.left = Binary_Tree(4)
    hi.left.right = Binary_Tree(5)


