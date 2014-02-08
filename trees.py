## Tree Data Structure ##





# Two ways to implement #
# 1- List of Lists
# 2- Classes (tree, nodes, edges)




# List of Lists Implementation (no classes!)

def binaryTree(root):
    return [root, [], [] ]

def getLeftChild(subtree):
    return subtree[1]

def getRightChild(subtree):
    return subtree[2]

def insertLeft(subtree, val):
    subtree[1] = val

def insertRight(subtree, val):
    subtree[2] = val

def getRootVal(subtree):
    return subtree[0]

def setRootVal(subtree, val):
    subtree[0] = val


r1 = 'root'
t1 = binaryTree(r1)
#print getLeftChild(t1)
#print getRootVal(t1)
insertRight(t1, binaryTree('child2'))
insertLeft(t1, binaryTree('child1'))
child1 = getLeftChild(t1)
insertRight(child1, binaryTree('child1a'))
insertLeft(child1, binaryTree('child1b'))

#print child1
#print getLeftChild(child1)

print t1

def printTree(tree):
    print tree[0]
    if tree[1] == []:
        return []
    elif tree[2] == []:
        return []
    else:
        return str(printTree(tree[1])) + '---' + str(printTree(tree[2]))


#print printTree(t1)






# Nodes + References Implementation (classes)


# Tree class which references root node only!
class BinaryTree(object):
    def __init__(self, root):
        self.rootNode = Node(root)

    def getRootNode(self):
        return self.rootNode


# Node class which holds root val, child1, and child2 node references
class Node(object):
    def __init__(self, rootval):
        self.root = rootval
        self.leftChild = None
        self.rightChild = None

    def getRoot(self):
        return self.root

    def setRoot(self, val):
        self.root = val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setLeftChild(self, val):
        self.leftChild = Node(val)

    def setRightChild(self, val):
        self.rightChild = Node(val)



b1 = BinaryTree('a')
r1 = b1.getRootNode()
r1.setLeftChild('b')
r1.setRightChild('c')

print r1.getRoot()
lc = r1.getLeftChild()
print lc.getRoot()
lc.setRightChild('d')
print lc.getRightChild().getRoot() 

rc = r1.getRightChild()
print rc.getRoot()
rc.setRightChild('f')
rc.setLeftChild('e')
print rc.getLeftChild().getRoot()
print rc.getRightChild().getRoot()
