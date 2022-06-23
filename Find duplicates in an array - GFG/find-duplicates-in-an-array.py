import collections

class Solution:
    def duplicates(self, arr, n): 
        c = collections.Counter(arr)
        ans = []
        for key, val in c.items():
            if val > 1:
                ans.append(key)
        
        if not ans:
            return [-1]
        return sorted(ans)
#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends