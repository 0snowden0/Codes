from stack import Stack
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
		
class Tree:
	def __init__(self,data):
		self.root = Node(data)
		
tree = Tree(1)
a = Node(2)
b= Node(3)
c = Node(4)
d = Node(5)
e = Node(6)
f = Node(7)
g = Node(8)
h = Node(9)

tree.root.right = f
tree.root.left = a
a.left = b
a.right = c
c.left = d
c.right = e
f.left = g
f.right = h

############################

def postorder(root):	
	stack = Stack()
	prev = None
	while True:
		while root:
			stack.push(root)
			root = root.left
		root = stack.top()
		if root.right == None or root.right == prev:
			stack.pop()
			print(root.data)
			prev = root
			root = None
			continue
		root = root.right
		if stack.top() == 'empty':
			break
			
postorder(tree.root)
			
		
				

