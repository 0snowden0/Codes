def towersOfHanoi(n,from_rod,to_rod,aux_rod):
	if n==1:
		print("Move disk 1 from",from_rod,"to",to_rod)
		return
	towersOfHanoi(n-1,from_rod,aux_rod,to_rod)
	print("Move disk",n,"from",from_rod,"to",to_rod)
	towersOfHanoi(n-1,aux_rod,to_rod,from_rod)
	
def main():
	print("We'll be printing the solution for the Towers Of Hanoi puzzle")
	n = input("Enter the number of disks : ")
	print('''From Disk	: A
To Disk		: C
Auxilary Disk	: B		''')
	towersOfHanoi(int(n),'A','C','B')
	
if __name__ == '__main__':
	main()
