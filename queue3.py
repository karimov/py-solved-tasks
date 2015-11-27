from linkedlist2 import Node

class Queue:
	def __init__(self):
	    self.length = 0
	    self.root = None
	def is_empty(self):
	    return self.length == 0
	def insert(self, data):
	    node = Node(data)
	    if self.root is None:
	    # If list is empty the new node goes fir
	       self.root = node
	    else:
	    	last = self.root
	    	while last.next:
	    		last = last.next
	    	# Append the new node
	    	last.next = node
	    self.length += 1
	def remove(self):
	    data = self.root.data
	    self.root = self.root.next
	    self.length -= 1
	    return data
        def front(self):
       	    return self.root
	  
class ImprovedQueue:
	def __init__(self):
	    self.length = 0
	    self.root = None
	    self.last = None
	def insert(self, data):
	    node = Node(data)
	    if self.length == 0:
	    	self.root = self.last = node
	    else:
	    	self.last.next = node
	    	self.last = node
	    self.length += 1
	def remove(self):
	    data = self.root.data
	    self.root = self.root.next
	    self.length -= 1
	    if self.length == 0:
	    	self.last = None
	    return data  
	    
	    
class PriorityQueue:
	def __init__(self):
	    self.items = []
	def insert(self, data):
	    self.items.append(data)
	def is_empty(self):
	    return not self.items
	def remove(self):
	    maxi = 0
	    for i in range(1, len(self.items)):
	    	if self.items[i] > self.items[maxi]: 
	    	   maxi = i
	    item = self.items[maxi]
	    del self.items[maxi]
	    return item	 	
	    
	    
class Golfer:
	def __init__(self, name, score):
            self.name = name
            self.score= score
	def __str__(self):
            return "{0:16}: {1}".format(self.name, self.score)
        def cmp(self, other):
            if self.score < other.score:
            	return 1
            if self.score > other.score:
               return -1
            return 0
	def __gt__(self, other):
	    return self.cmp(other)>0
