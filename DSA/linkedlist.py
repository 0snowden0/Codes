class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class linkedList():
	def __init__(self):
		self.head = None
			
	def Push(self,data):
		if self.head is None:
			self.head = Node(data)
			return
		
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def Pop(self):
		if self.head is None:
			return 'empty'
		current = self.head
		new_head = self.head.next
		current.next = None
		self.head = new_head
		return current.data
		
	def Top(self):
		return self.head
		
