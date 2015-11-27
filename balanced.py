from stack import Stack

def parChecker_v2(symbolstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol in "0123456789":
            index += 1
            continue
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    return False

def matches(open, close):
    opener = "({["
    closer = ")}]"
    return opener.index(open) == closer.index(close)


def parChecker_v1(symbolstring):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolstring) and balanced:
        symbol = symbolstring[index]
        if symbol in "0123456789":
            index += 1
            continue
        if symbol in "({[":
            s.push(symbol)
        if symbol in "]})":
            top = s.pop()
            if not matches(top, symbol):
                balanced = False
        index += 1
    if balanced and s.is_empty():
        return True
    return False
