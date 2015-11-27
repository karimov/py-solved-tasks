from stack import Stack
import re

def infixTopostfix(infixExpression):
    reg = re.search(r'[!@#$%^&\t\s\{\[\]\}]', infixExpression)
    if reg:
        raise Exception("uncorrect infix expression")

    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack =Stack()
    postfixList = []
    tokenList =  re.findall(r'[^!@#$%^&\t\s\{\[\]\}]', infixExpression)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token is "(":
            opstack.push(token)
        elif token is ")":
            topToken = opstack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.is_empty()) and (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    while not opstack.is_empty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)
