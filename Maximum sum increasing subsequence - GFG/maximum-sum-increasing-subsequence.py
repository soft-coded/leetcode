import math

#User function Template for python3
class Solution:
	def maxSumIS(self, arr, n):
# 		def recur(index, prev, memo):
# 		    if index == len(arr):
# 		        return 0
# 		    memo_str = "{},{}".format(index, prev)
# 		    if memo_str in memo:
# 		        return memo[memo_str]
		       
# 		    not_pick = recur(index + 1, prev, memo)
# 		    pick = -math.inf
# 		    if prev < arr[index]:
# 		        pick = arr[index] + recur(index + 1, arr[index], memo)
		    
# 		    ans = max(pick, not_pick)
# 		    memo[memo_str] = ans
# 		    return ans
		
# 		return recur(0, -math.inf, {})  
    
        max = 0
        msis = [0 for x in range(n)]
    
        # Initialize msis values
        # for all indexes
        for i in range(n):
            msis[i] = arr[i]
    
        # Compute maximum sum 
        # values in bottom up manner
        for i in range(1, n):
            for j in range(i):
                if (arr[i] > arr[j] and
                    msis[i] < msis[j] + arr[i]):
                    msis[i] = msis[j] + arr[i]
    
        # Pick maximum of
        # all msis values
        for i in range(n):
            if max < msis[i]:
                max = msis[i]
    
        return max

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends