class Solution:
	def overlappedInterval(self, intv):
		intv.sort()
		lo = intv[0][0]
		hi = intv[0][1]
		ans = []
		for i in range(1, len(intv)):
		    if intv[i][0] <= hi:
		        hi = max(hi, intv[i][1])
		    else:
		        ans.append([lo, hi])
		        lo = intv[i][0]
		        hi = intv[i][1]
		ans.append([lo, hi])
	    return ans
		    

#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends