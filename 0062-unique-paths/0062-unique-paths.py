class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#       memo = {}
#       def recur(i, j):
#         if i == 0 and j == 0:
#           return 1
#         if i < 0 or j < 0:
#           return 0
#         memo_str = f"{i},{j}"
#         if memo_str in memo:
#           return memo[memo_str]
        
#         up = recur(i - 1, j)
#         left = recur(i, j - 1)
#         memo[memo_str] = up + left
#         return memo[memo_str]
      
#       return recur(m - 1, n - 1)

      dp = [[1] * n for _ in range(m)]
      for i in range(1, m):
        for j in range(1, n):
          dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
      
      return dp[m - 1][n - 1]