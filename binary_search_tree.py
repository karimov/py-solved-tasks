'''
We need to have two classes
for implementation of binary search tree
'''

# BinarySearchTree 
import stack

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def height(self):
        return self._height(self.root)

    def _height(self, currentNode):
        if not currentNode:
            return -1
        else:
            return 1 + max(self._height(currentNode.leftChild), self._height(currentNode.rightChild))

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, parent=currentNode)
        else:
            leftChild = currentNode.leftChild
            rightChild = currentNode.rightChild
            currentNode.replaceNodeData(key, value, leftChild, rightChild)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        elif currentNode.key < key:
            return self._get(key, currentNode.rightChild)
        elif currentNode.key == key:
            return currentNode

    def delete(self, key):
        if self.size > 1:
            nodeToremove = self._get(key, self.root)
            if nodeToremove:
                self.remove(nodeToremove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, currentNode):
        if currentNode.isLeaf(): # this node has no child
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): # interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                                        currentNode.leftChild.key,
                                        currentNode.leftChild.payload,
                                        currentNode.leftChild.leftChild,
                                        currentNode.rightChild.rightChild
                                        )
            if currentNode.hasRightChild():
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightCHild = currentNode.rightCHild
                else:
                    currentNode.replaceNodeData(
                                        currentNode.rightChild.key,
                                        currentNode.rightChild.payload,
                                        currentNode.rightChild.leftChild,
                                        currentNode.rightChild.rightChild
                                        )
    def inorder(self):
        current = self.root
        pStack = stack.Stack()
        while pStack.size() > 0 or current != None:
            if current:
                pStack.push(current)
                current = current.leftChild
            else:
                current = pStack.pop()
                print(current.key)
                current = current.rightChild

# non-recursive inorder traversal using with findSuccessor()

    def inorder_nonrecursive(self):
        current = self.root
        while current.hasLeftChild():
            current = current.leftChild
        succ = current.findSuccessor()
        stop = False
        while not stop:
            if succ:
                print(current.key)
                current = succ
                succ = succ.findSuccessor()
            else:
                print(current.key)
                stop = True

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, k):
        return self.get(k)

    def __setitem__(self,k,v):
        self.put(k,v)

    def __contains__(self, k):
        if self._get(k, self.root):
            return True
        else:
            return False

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


# TreeNode

class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.successor = None

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

# nodes maintians the references to its successor

    def updateSuccessor(self):
        self.successor = self.findSuccessor()

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = se;f.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem
