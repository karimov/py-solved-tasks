from linkedlist2 import Node

class ImprovedQueue:
    def __init__(self):
        self.root = None
        self.last = None
        self.length = 0
    def is_empty(self):
        return self.length == 0
    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = self.last = node
        if node.data > self.root.data:
            node.next = self.root
            self.root = node
        if node.data < self.last.data:
            self.last.next = node
            self.last = node
        if node.data > self.last.data and node.data < self.root.data:
            temp = self.root
            p = self.root.next
            while p != None:
                if p.data > node.data:
                    temp = temp.next
                    p = p.next
                break
            node.next = temp.next
            temp.next = node
        self.length += 1
