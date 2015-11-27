
def toStr(number, base):
    convertString = '0123456789ABCDEF'
    if number < base:
        return convertString[number]
    else:
        return toStr(number//base, base) + convertString[number%base]

def theSum(listNumbers):
    if len(listNumbers) == 1:
        return listNumbers[0]
    else:
        return listNumbers[0] + theSum(listNumbers[1:])

def reverse(aString):
    if len(aString) == 1:
        return aString[0]
    else:
        return reverse(aString[1:]) + aString[0]

def stringFix(aString):
    aString = aString.replace(" ", "").replace("'", "")
    return aString.lower()

def isPal(aString):
    aString = stringFix(aString)
    if len(aString) == 1 or len(aString) == 0:
        return True
    if aString[0] != aString[-1]:
        return False
    else:
        return isPal(aString[1:-1])

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def reverseList(aList):
    if len(aList) == 1:
        return [aList[0]]
    else:
        return reverseList(aList[1:]) + [aList[0]]


def fibonacci_seq(n):
    if n == 0:
        return n
    a,b = 0, 1
    index = 1
    while index < n:
        a,b = b, a+b
        index += 1

    return b

def recursive_fibonacci_seq(n):
    if n == 1or n ==0:
        return n
    else:
        return recursive_fibonacci_seq(n-1) + recursive_fibonacci_seq(n-2)
