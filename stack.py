from node import Node

class Stack:
    def __init__(self, name=None):
        self.items = []
        self.name = name
    def __str__(self):
        return str(self.name)
    def __repr__(self):
        return repr(self.name)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def remove(self):
        self.items.pop()

class Stackv2:
    def __init__(self):
        self.bottom = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def puhh(self, item):
        bottom = self.bottom
        node = Node(item)
        if bottom == None:
            self.bottom = node
            self.length += 1
        else:
            bottom.setNext(node)
            self.length += 1

    def pop(self):
        bottom = self.bottom
        basement = None
        topFound = False
        while bottom != None and not topFound:
            if bottom.getNext() == None:
                topFound = True
            else:
                basement = bottom
                bottom = bottom.getNext()

        if basement == None:
            self.bottom = bottom.setNext()
            self.length -= 1
        else:
            basement.setNext(None)
            self.length -= 1

    def size(self):
        if self.size < 0:
            return 0
        return self.size
