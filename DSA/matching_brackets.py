from stack import Stack

def check_paranthesis(lst):

	stack = Stack()	
	
	for item in lst:
		if item == '(':
			stack.push('(')
			continue
		if item == '{':
			stack.push('{')
			continue
		if item == '[':
			stack.push('[')
			continue
		if item == ')':
			check = stack.pop()
			if check == '(':
				continue
			else:
				print('The brackets dosent match, please check!')
				return
		if item == '}':
			check = stack.pop()
			if check == '{':
				continue
			else:
				print('The brackets dosent match, please check!')
				return
		if item == ']':
			check = stack.pop()
			if check == '[':
				continue
			else:
				print('The brackets dosent match, please check!')
				return
	print('The brackets match perfectly!')
		
def main():
	print("enter the bracket list to check")
	lst = list(input().split())
	check_paranthesis(lst)
	
if __name__ == '__main__':
	main()
	
