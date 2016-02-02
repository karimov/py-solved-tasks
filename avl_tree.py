'''
AVL - balanced Binary Search Tree
Big-O always is logN
'''

'''
Once we have added new leaf node
we have to update balance factor
of its parent
'''

'''
AVL will subclass of BinarySearchTree class
'''

'''
we write new helper method
updateBalance
'''

def _put(self, key, val, currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
            self._put(key, val, currentNode.leftChild)
        else:
            currentNode.leftChild = TreeNode(key, val, parent=currentNode)
            self.updateBalance(currentNOde.leftChild)
    else:
        if currentNode.hasRightChild():
            self._put(key, val, currentNode.rightChild)
        else:
            currentNode.rightChild = TreeNode(key, val, parent=currentNode)
            self.uodateBalance(currentNode.rightChild)

def updateBalance(self, node):
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
            node.parent.balanceFactor += 1
        elif node.isRightChild():
            node.parent.balanceFactor -= 1

        if node.parent.balanceFactor != 0:
            self.updateBalance(node.parent)



# rotation code

def rotationLeft(self, rotRoot):
    newRoot = rotRoot.rightChild
    rotRoot.rightChild = newRoot.leftChild
    if newRoot.leftChild != None:
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():
            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
    newRoot.leftChild = rotRoot # basicleft rotarion line
    rotRoot.parent = newRoot

    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(0, newRoot.balanceFactor)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(0, rotRoot.balanceFactor)

def rotationRight(self, rotRoot):
    newRoot = rotRoot.leftChild
    rotRoot.leftChild = newRoot.rightChild
    if newRoot.rightChild != None:
        newRoot.rightChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isLeftChild():
            rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChuld = newRoot
    newRoot.rightChild = rotRoot
    rotRoot.parent = newRoot

    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(0, newRoot.balanceFactor)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(0, rotRoot.balanceFactor)


def rebalance(self, node):
    if node.balanceFactor < 0:
        if node.rightChild.balanceFactor > 0:
            self.rotationRight(node.rightChild)
            self.rotationLeft(node)
        else:
            self.rotationLeft(node)
    elif node.balanceFactor > 0:
        if node.leftChild.balanceFactor < 0:
            self.rotationLeft(node.leftChild)
            sekf.rotationRight(node)
        else:
            self.rotationRight(node)
