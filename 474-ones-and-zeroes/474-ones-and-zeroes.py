def count01(s):
  zeros = ones = 0
  for char in s:
    if char == '1':
      ones += 1
    else:
      zeros += 1
  return zeros, ones

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        values = []
        for st in strs:
          zeros, ones = count01(st)
          if zeros <= m and ones <= n:
              values.append((zeros, ones))
            
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for zeros, ones in values:
          for i in range(m, zeros - 1, -1):
            for j in range(n, ones - 1, -1):
              dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
        
        
        