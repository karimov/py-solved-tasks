class Node:
	def __init__(self, data, next=None):
	    self.data = data
	    self.next = next
	def __str__(self):
	    return str(self.data)
	def get_data(self):
	    return self.data
	def set_data(self, data):
	    self.data = data
	def get_next(self):
	    return self.next
	def set_next(self, next):
	    self.next = next
 	    
class LinkedList:
      def __init__(self, root=None):
      	  self.size = 0
      	  self.root = root
      def get_size(self):
      	  return self.size
      def add(self, data):
     	  new_node = Node(data, self.root)
     	  self.root = new_node
     	  self.size += 1
      def remove(self, data):
      	  this_node = self.root
      	  prev_node = None
      	  while this_node:
      	  	if this_node.get_data() == data:
      	  	   if prev_node:
      	  	      prev_node.set_next(this_node.get_next())
      	  	   else:
      	  	      self.root = this_node
      	  	      self.seize -= 1
      	  	      return True    #data removed
      	  	else:
      	  	     prev_node = this_node
      	  	     this_node = this_node.get_next()
      	  return False  # data noi found
      def find(self, data):
      	  this_node = self.root
      	  while this_node:
      	  	if this_node.get_data() == data:
      	  	   return data
      	  	else:
      	  	    this_node = this_node.get_next()
      	  return None	      
