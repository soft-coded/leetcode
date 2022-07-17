class Solution:
  def isMatch(self, text: str, pattern: str) -> bool:
#       memo = {}
#       def recur(i, j):
#         if i < 0 and j < 0:
#           return True
#         if j < 0:
#           for k in range(i + 1):
#             if pattern[k] != '*':
#               return False
#           return True
#         if i < 0:
#           return False
#         memo_str = f"{i},{j}"
#         if memo_str in memo:
#           return memo[memo_str]
        
#         if pattern[i] == text[j] or pattern[i] == '?':
#           memo[memo_str] = recur(i - 1, j - 1)
#         elif pattern[i] == '*':
#           memo[memo_str] = recur(i - 1, j) or recur(i, j - 1)
#         else:
#           memo[memo_str] = False
          
#         return memo[memo_str]
        
#       return recur(len(pattern) - 1, len(text) - 1)
      
      n = len(pattern)
      m = len(text)
      dp = [[False] * (m + 1) for _ in range(n + 1)]
      
      dp[0][0] = True
      
      for i in range(1, n + 1):
        is_star = True
        for j in range(i):
          if pattern[j] != '*':
            is_star = False
            break
        dp[i][0] = is_star
        
      for i in range(1, n + 1):
        for j in range(1, m + 1):
          if pattern[i - 1] == text[j - 1] or pattern[i - 1] == '?':
            dp[i][j] = dp[i - 1][j - 1]
          
          elif pattern[i - 1] == '*':
            dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
          
          else:
            dp[i][j] = False
      
      return dp[n][m]
      




















