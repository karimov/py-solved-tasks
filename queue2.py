class Queue:
    def __init__(self):
        self.length = 0
        self.items = []
        self.root = None
    def isEmpty(self):
        return not self.items
    def insert(self, obj):
        self.items.append(obj)
        self.root = self.items[0]
        self.length += 1
    def remove(self):
        if self.isEmpty():
            return None
        else:
            data = self.items[0]
            del self.items[0]
          #  self.root = self.items[0]
            self.length -= 1
            return data
    def front(self):
        return self.items[0]
