#User function Template for python3

class Solution:
    def factorial(self, n):
        ans = 1
        while n > 1:
            ans *= n
            n -= 1
        return str(ans)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends