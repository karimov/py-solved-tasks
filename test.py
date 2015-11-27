class ImprovedQueue:
    def _init__(self, data, root=None, last=None):
        self.data = data
        self.root = root
        self.last = last
    def __init__(self):
        self.root = None
        self.last = None
    def __str__(self):
        return str(self.root),str(self.last)
