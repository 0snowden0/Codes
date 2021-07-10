def fibonacci(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1)+fibonacci(n-2)
	
def main():
	print("We will be printing the fibonacci series till the number 'n' here")
	n = int(input("Enter n : "))
	for i in range(n+1):
		print(fibonacci(i), ' ')
		
if __name__ == '__main__':
	main()
		
