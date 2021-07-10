def max_xor(a,x,m):
	maxi,data = -1,None
	for i in a:
		val = i^x
		if val > maxi:
			maxi,data = val,i
	if i>m:
		return -1
	else:
		return val
	
def main():
	noofcases = int(input())
	for i in range(noofcases):
		length = input()
		lst = list(map(int,input().split()))
		q = int(input())
		for i in range(q):
			x,m = map(int, input().split())
			print(max_xor(lst,x,m))
			
if __name__ == '__main__':
	main()
