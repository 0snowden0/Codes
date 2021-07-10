def binaryStrings(s,n):
	if n == 0:
		print(str(s))
		return
	for i in range(2):
		s[n-1] = i
		binaryStrings(s,n-1)
		
def main():
	print("We wil be printing all the binary strings of 'n' length here")
	n = int(input("Enter n : "))
	s=[]
	for i in range(n):
		s.append(None)
	binaryStrings(s,n)
	
if __name__ == '__main__':
	main()
