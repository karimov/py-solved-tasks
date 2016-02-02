from binarytree import BinaryTree 
from stack import Stack
import operator

def buildParseTree(fpexp):
#   fplist = [ch for ch in fpexp if ch != " "]
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == 'not':
            currentTree = pStack.pop()
            currentTree.leftChild = None
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i not in ['+', '-', '*', '/', ')', 'and', 'or']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/', 'or', 'and']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
     opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

     leftC = parseTree.getLeftChild()
     rightC = parseTree.getRightChild()

     if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
     else:
        return parseTree.getRootVal()
