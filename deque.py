
class Deque:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def addFront(self, item):
        self.item.append(item)

    def addRear(self, item):
        self.item.insert(0, item)

    def removeFront(self):
        return self.item.pop()

    def removeRear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)
