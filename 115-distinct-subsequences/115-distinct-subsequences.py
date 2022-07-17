class Solution:
    def numDistinct(self, s: str, t: str) -> int:
      lt = len(t)
      ls = len(s)
#       memo = {}
#       def recur(i, j):
#         if j < 0:
#           return 1
#         if i < 0:
#           return 0
#         memo_str = f"{i},{j}"
#         if memo_str in memo:
#           return memo[memo_str]

#         if s[i] == t[j]:
#           memo[memo_str] = recur(i - 1, j - 1) + recur(i - 1, j)
#         else:
#           memo[memo_str] = recur(i - 1, j)
          
#         return memo[memo_str]

#       return recur(ls - 1, lt - 1)
  
      dp = [[0] * (lt + 1) for _ in range(ls + 1)]
      
      for i in range(ls + 1):
        dp[i][0] = 1
        
      for i in range(1, ls + 1):
        for j in range(1, lt + 1):
          if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
          else:
            dp[i][j] = dp[i - 1][j]
      
      return dp[ls][lt]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    