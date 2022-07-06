#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
	    ans = []
	    
	    def calc_sum(i, cur_sum):
	        if i == len(arr):
	            ans.append(cur_sum)
	            return
	           
            calc_sum(i + 1, cur_sum + arr[i])
            calc_sum(i + 1, cur_sum)
        
        calc_sum(0, 0)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends