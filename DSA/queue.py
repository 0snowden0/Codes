from linkedlist import linkedList

class Queue:
	def __init__(self):
		self.llist = linkedList()
		
	def EnQueue(self,data):
		self.llist.enq(data)
		return
		
	def DeQueue(self):
		return self.llist.dq()
		
	def isEmptyQueue(self):
		return self.llist.checkempty()



		
