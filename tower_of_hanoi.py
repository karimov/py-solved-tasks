from stack import Stack

def heightStack(height, nameStr):
    h = Stack(nameStr)
    while height != 0:
        h.push(height)
        height -= 1

    return h

def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fromPole, toPole):
    toPole.push(fromPole.pop())
    print("Moving disk from", fromPole, "to", toPole)
