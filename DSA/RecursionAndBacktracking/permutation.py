#This code for permutation of a word, namely 'History'
#will be done using the concept of backtracking
#Initially we define the function by giving the left end of the string,
#the right end of the string and the string itself as a list as arguments
def permutation(l,r,s):
	#here we test for the base case, i.e when the left end of the string coincides with the right end,
	#this happens because we'll be incrementing a variable which points to the left end one by one till we
	#reach the right end
	if(l==r-1):
		#We join the list back to a string and print it
		k = ''.join(s)
		print(k)
		return
	#We are defining a for loop for incrementing the left pointer one by one till it reaches the right end
	for i in range(l,r):
		#This is the key concept of accomplishing permutation
		#we swap the left pointer with the folloing elements one by one and then
		#permute the rest of the string, i.e the string following the current left pointer, through recursion.
		#Then we reverse the swap and go on to swap with the next element
		s[l] , s[i] = s[i] , s[l]
		#calling the function again by incrementing the left pointer by 1 to permute the rest of the string till we reach
		#right end
		permutation(l+1, r,s)
		#now we're swapping the elements back
		s[l],s[i] = s[i],s[l]

string = 'History'
permutation(0,len(string),list(string))
