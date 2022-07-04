#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        dic = {}
        mx = sm = 0
        for i in range(n):
            sm += arr[i]
            if sm == 0:
                mx = i + 1
            else:
                if sm in dic:
                    mx = max(mx, i - dic[sm])
                else:
                    dic[sm] = i
        return mx
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends