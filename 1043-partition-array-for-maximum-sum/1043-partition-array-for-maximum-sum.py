from sys import setrecursionlimit
setrecursionlimit(10**7)
from functools import lru_cache

def calc(arr, i, j):
  mx = 0
  for ind in range(i, j + 1):
    mx = max(mx, arr[ind])
  
  num = j - i + 1
  return mx * num


class Solution:
  def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
    n = len(arr)
#     # memo = {}
#     @lru_cache(None)
#     def recur(i):
#       if i >= n:
#         return 0
#       # if i in memo:
#         # return memo[i]
      
#       # memo[i] = 0
#       ans = 0
#       for ind in range(i, min(i + k, n)):
#         # memo[i] = max(memo[i], recur(ind + 1) + calc(arr, i, ind))
#         ans = max(ans, recur(ind + 1) + calc(arr, i, ind))
      
#       # return memo[i]
#       return ans
    
#     return recur(0)


#     dp = [0] * (n + 1)
  
#     for i in range(n - 1, -1, -1):
#       for ind in range(i, min(i + k, n)):
#         dp[i] = max(dp[i], dp[ind + 1] + calc(arr, i, ind))
      
#     return dp[0]
      
    K = k
    N = len(arr)
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        curMax = 0
        for k in range(1, min(K, i) + 1):
            curMax = max(curMax, arr[i - k])
            dp[i] = max(dp[i], dp[i - k] + curMax * k)
    return dp[N]
