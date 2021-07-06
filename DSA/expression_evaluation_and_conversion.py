from stack import Stack
import operator

def infix_to_postfix(lst):
	expression = ''
	precedense = {'+':1, '-':1, '*':2, '/':2}
	stack = Stack()
	for item in lst:
		if item in precedense:
			while (stack.top() == 'empty') or (stack.top() in ['(', '{', '[']) or (precedense[stack.top()] >= precedense[item]):
				if stack.top() in ['(', '{', '[']:
					break
				k = stack.pop()
				if k == 'empty':
					break
					
				expression = expression+k
			stack.push(item)
		elif (item in [')', '}', ']']):
			while stack.top() not in ['(', '{', '[']:
				expression = expression+stack.pop()
			else:
				stack.pop()
		elif item in ['(', '{', '[']:
			stack.push(item)
			
		else:
			expression = expression+item
			
	while stack.top() != 'empty':
		expression=expression+stack.pop()
		
	return expression
	
def postfix_evaluation(lst):
	stack = Stack()
	precedense = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	for item in lst:
		if item in precedense:
			i = stack.pop()
			j = stack.pop()
			stack.push(precedense[item](int(j),int(i)))
		else:
			stack.push(item)
			
	return stack.pop()

			

			
			
		 
		
