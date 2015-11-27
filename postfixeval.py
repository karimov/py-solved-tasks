from stack import Stack

def postfixEval(postfixExp):
    operandstack = Stack()
    tokenList = postfixExp.split()
    for token in tokenList:
        if token in "0123456789":
            operandstack.push(int(token))
        else:
            operand2 = operandstack.pop()
            operand1 = operandstack.pop()
            result = doMath(token, operand1, operand2)
            operandstack.push(result)
    return operandstack.pop()


def doMath(operator, operand1, operand2):
    operators = {"*":0, "/":1, "+":2, "-":3}
    if operators[operator] == 0:
        return int(operand1) * int(operand2)
    elif operators[operator] == 1:
        return int(operand1) // int(operand2)
    elif operators[operator] == 2:
        return int(operand1) + int(operand2)
    else:
        return int(operand1) - int(operand2)

def infixEval(infixExpression):
    prec = {}
    pec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec['-'] = 2
    prec["("] = 1
    opstack = Stack()
    operandstack = Stack()
    tokenList = infixExpression.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            operandstack.push(token)
        elif token is "(":
            opstack.push(token)
        elif token is ")":
            topToken = opstack.pop()
            while topToken != "(":
                operand2 = operandstack.pop()
               operand1 = operandstack.pop()
                result = doMath(topToken, operand1, operand2)
                operandstack.push(result)
                topToken = opstack.pop()
        elif opstack.is_empty():
            opstack.push(token)
        else:
            while (not opstack.is_empty()) and (prec[opstack.peek()] >= prec[token]):
                operand2 = operandstack.pop()
                operand1 = operandstack.pop()
                operator = opstack.pop()
                result = doMath(operator, operand1, operand2)
                operandstack.push(result)
                opstack.push(token)
            opstack.push(token)

    while not opstack.is_empty():
        operator = opstack.pop()
        operand2 = operandstack.pop()
        operand1 = operandstack.pop()
        result = doMath(operator, operand1, operand2)
        operandstack.push(result)

    return operandstack.pop()
