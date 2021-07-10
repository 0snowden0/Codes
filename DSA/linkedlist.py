class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class linkedList():
	def __init__(self):
		self.head = None
		self.rear = None
	#STACK LINKEDLIST BEGIN#		
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
	#STACK LINKEDLIST END#
	
	#QUEUE LINKEDLIST BEGIN#
	def enq(self,data):
		current = self.rear
		new_node = Node(data)
		if current is None:
		 	self.head = new_node
		 	self.rear = new_node
		 	return
		 
		current.next = new_node
		self.rear = new_node
		 
	def dq(self):
		current = self.head
		self.head = current.next
		current.next = None
		if self.head == None:
			self.rear = None
		return current.data
		
	def checkempty(self):
		if self.head == None:
			return True
		else:
			return False
