class Node:
      def __init__(self, cargo=None, next=None):
          self.cargo = cargo
          self.next  = next
      def __str__(self):
          return str(self.cargo)
          
          
def print_list(node):
    while node is not None:
          print node, " "
          node = node.next
    print()
          
          
def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print head,"  "
