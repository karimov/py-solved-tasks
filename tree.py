class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)
    def in_order(self):
        if self.left is not None:
            for value in self.left.in_order():
                yield value
        yield self.value
        if self.right is not None:
            for value in self.right.in_order():
                yield value
    def preorder(self):
        if self is not None:
            print(self)
            preorder(self.left)
            preorder(self.right)
