def checkSortedArray(A,l,r):
	if l==r-1:
		print("The Array is Sorted")
		return
	if A[l]<A[l+1]:
		checkSortedArray(A,l+1,r)
	else:
		print("The Array is NOT Sorted")
		return
		
def main():
	print("We will be check the entered List of numbers is in ascending order, please give the input as a space separated list")
	A = list(map(int, input("Enter The list here : ").split()))
	checkSortedArray(A,0,len(A)-1)
	
if __name__ == '__main__':
	main()
	
