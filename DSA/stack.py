from linkedlist import linkedList

class Stack:
	def __init__(self):
		self.llist = linkedList()
		
	def pop(self):
		return self.llist.Pop()
		
	def push(self,data):
		return self.llist.Push(data)
		
	def top(self):
		node = self.llist.Top()
		if node is None:
			return 'empty'
		else:
			return node.data
		

		
		
