class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def recur(i, j):
          if i < 0 and j < 0:
            return 0
          if i < 0:
            return j + 1
          if j < 0:
            return i + 1
          
          memo_str = f"{i},{j}"
          if memo_str in memo:
            return memo[memo_str]
          
          if word1[i] == word2[j]:
            return recur(i - 1, j - 1)
          
          ans = min(recur(i - 1, j), recur(i, j - 1), recur(i - 1, j - 1)) + 1
          memo[memo_str] = ans
          return ans
          
        return recur(len(word1) - 1, len(word2) - 1)
          
#         n = len(word1)
#         m = len(word2)
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
        
#         for i in range(1, m + 1):
#           dp[0][i] = m
#         for i in range(1, n + 1):
#           dp[i][0] = n
          
#         for i in range(1, n + 1):
#           for j in range(1, m + 1):
#             if word1[i - 1] == word2[j - 1]:
#               dp[i][j] = dp[i - 1][j - 1]
#             else:
#               dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
#         return dp[n][m]
        
          
          