#The traversing begins by passing the root of the tree to the function
def postorder_without_recursion(root):
	#Here we are creating a stack to push the root nodes into the stack as we are traversing the tree
	stack = Stack()
	#Since we are traversing tree in postorder, we must keep track of the fact that whether the right node,
	#i.e the right child of the current parent was already visited, for that purpose, we keep this variable prev 
	prev = None
	#We are starting a while loop which will end once the stack is empty.This condition is provided at the end of this while loop
	while True:
		#We are starting a while loop here which will continue looping towards the left tree until a leaf whose
		#left node is None is encountered,i.e a node which has only right child
		while root:
			#As we are traversing the left tree, we'll be pushing these nodes into the stack
			stack.push(root)
			#And on to the next left node we go
			root = root.left
		#We'll be taking the top element of the stack
		root = stack.top()
		#Now we'll be only printing this node if either the current node, i.e one at the top of the stack is a leafnode,
		#i.e when the right node of the current node is a None or if the right node of the current node is already visited.
		#We will be tracking this property , using the prev variable. If the right child of the current node is a previously 
		#visited node, then we print this current node and pop it off the the stack
		if root.right == None or root.right == prev:
			#popping the current node off the stack
			stack.pop()
			print(root.data)
			#setting the current node as prev so that it's parent can detect that it's been 
			#already executed and act accordingly
			prev = root
			#As we won't want to execute the current node's left children, as obviously 
			#it's been already executed , we set it to None
			root = None
			continue
		#if the above 'If' condition is not true, i.e if we're not looking at a leaf node and we're
		#not looking at a node who's right child has not yet been visited, we go visit the right node in post-order
		root = root.right
		#If the stack is empty, our work is done. We break off the loop
		if stack.isEmpty():
			break
