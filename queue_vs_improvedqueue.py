class Queue:
	def __init__(self):
	    self.items = []
	def insert(self, obj):
	    self.items.append(obj)
	def is_empty(self):
	    return not self.items
	def remove(self):
	    #if self.is_empty():
	    #	return "Empty"
	    #else: 
	    	#obj = self.items[0]
	    	del self.items[0]
	   # return obj
	    
	    
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

    
	    	last = self.last
	    	self.last = node
	    	last.next = node
	    	self.length += 1
	def remove(self):
	    #data = self.root.data
	    self.root = self.root.next
	    self.length -= 1
	    if self.root == None:
	    	self.last = None
	    #return data
	    
