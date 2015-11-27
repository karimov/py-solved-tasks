from deque import  Deque

def palCheck(str):
    d = Deque()
    str = str.replace(" ", "").replace("\n", "")
    for elem in str:
        d.addFront(elem)

    equal = True
    while d.size() > 1 and equal:
        front = d.removeFront()
        rear = d.removeRear()
        if front != rear:
            equal = False

    return equal
