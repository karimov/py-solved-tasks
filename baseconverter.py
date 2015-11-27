from stack import Stack

def baseConverter(decimal, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decimal >0:
        remainder = decimal % base
        remstack.push(remainder)
        decimal //= base

    newString = ""
    while not remstack.is_empty():
        newString += digits[remstack.pop()]

    return newString
