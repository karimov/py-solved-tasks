'''
Tree Traversals

1. preorder traversal
2. inorder traversal
3. postorder tracersal
'''

#preorder travelsal
#implemented as a external function

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#internal method of class

def preorder_method(self):
    print(self.key)
    if self.leftChild:
        self.getLeftChild().preorder()
    if self.rightChild:
        self.getRightChild().preorder()


# postorder tracersal 
# implemented as an external function

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# useage postorder traversal
# to evaluate parse tree

def postorderEval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    res1 = None
    res2 = None
    if tree:
        res1 = postorderEval(tree.getLeftChild())
        res2 = postorderEval(tree.getRightChild())
        if res1 and res2:
            return operas[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

# inorder traversal

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# useage inorder traversal in parse tree
# to recover original expression

def printExp(tree):
    sval = ''
    if tree:
        sval = '(' +printExp(tree.getLeftChild())
        sval = sval + str(tree.getRootVal())
        sval = sval + printExp(tree.getRightChild())+ ')'

    return sval
