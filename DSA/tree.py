from stack import Stack
from queue import Queue
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
class Tree:
	def __init__(self,data):
		self.root = Node(data)
		
	def insert_using_level_order(self,data):
		new_node = Node(data)
		queue = Queue()
		if self.root:
			queue.EnQueue(self.root)
		while not queue.isEmptyQueue():
			root = queue.DeQueue()
			if root.left is None:
				root.left = new_node
				return
			else:
				queue.EnQueue(root.left)
			if root.right is None:
				root.right = new_node
				return
			else:
				queue.EnQueue(root.right)
		
tree = Tree(0)
for i in range(1,10):
	tree.insert_using_level_order(i)
#a = Node(2)
#b= Node(3)
#c = Node(4)
#d = Node(5)
#e = Node(6)
#f = Node(7)
#g = Node(8)
#h = Node(9)

#tree.root.right = f
#tree.root.left = a
#a.left = b
#a.right = c
#c.left = d
#c.right = e
#f.left = g
#f.right = h

############################

def postorder(root):	
	stack = Stack()
	prev = None
	while True:
		while root:
			stack.push(root)
			root = root.left
		if stack.top() == 'empty':
			break
		root = stack.top()
		if root.right == None or root.right == prev:
			stack.pop()
			print(root.data)
			prev = root
			root = None
			continue
		root = root.right
			
postorder(tree.root)

			
####################################

def levelorder(root):
	queue = Queue()
	if root == None:
		return
	queue.EnQueue(root)
	while(not queue.isEmptyQueue()):
		root = queue.DeQueue()
		print(root.data)
		if root.left:
			queue.EnQueue(root.left)
		if root.right:
			queue.EnQueue(root.right)
			
#levelorder(tree.root)
	

##################################

def maxnode(root):
	maxi = None
	if root:
		root_data = root.data
		leftmax = maxnode(root.left)
		rightmax = maxnode(root.right)
		if root_data and leftmax and rightmax:
			maxi = max(root_data,leftmax,rightmax)
		else:
			maxi = root_data
	return maxi
		
##########################################

def maxinlevelorder(root):
	maxi = None
	queue = Queue()
	if root == None:
		return
	queue.EnQueue(root)
	while(not queue.isEmptyQueue()):
		root = queue.DeQueue()
		left = root.left
		right = root.right
		if left:
			queue.EnQueue(root.left)
		if right:
			queue.EnQueue(root.right)
		if maxi is None:
			maxi = root.data
		elif root.data>maxi:
			maxi = root.data		
	print(maxi)
	
##############################################

def searchbinary(data,root):
	if root:
		if data == root.data:
			return True
		if searchbinary(data,root.left):
			return True
		else:
			return searchbinary(data,root.right)
	else:
		return False
		
		
		
				

