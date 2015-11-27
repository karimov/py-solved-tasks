from stack import Stack

def devideby2(decimal):
    s = Stack()
    while decimal > 0:
        rem = decimal % 2
        s.push(rem)
        decimal //= 2

    res = ''
    while not s.is_empty():
        res += str(s.pop())

    return res
