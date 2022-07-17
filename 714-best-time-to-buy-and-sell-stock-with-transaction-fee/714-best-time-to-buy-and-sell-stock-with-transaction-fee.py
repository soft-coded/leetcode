class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    n = len(prices)
#     memo = {}
#     def recur(i, can_buy):
#       if i == n:
#         return 0
#       memo_str = f"{i},{can_buy}"
#       if memo_str in memo:
#         return memo[memo_str]
        
#       if can_buy:
#         memo[memo_str] = max(recur(i + 1, False) - prices[i], recur(i + 1, True))
#       else:
#         memo[memo_str] = max(recur(i + 1, True) + prices[i] - fee, recur(i + 1, False))
#       return memo[memo_str]
        
#     return recur(0, True)  
    
    dp = [[0] * 2 for _ in range(n + 1)]
    
    for i in range(n - 1, -1, -1):
      for j in range(1, -1, -1):
        if j:
          dp[i][j] = max(dp[i + 1][0] - prices[i], dp[i + 1][1])
        else:
          dp[i][j] = max(dp[i + 1][1] + prices[i] - fee, dp[i + 1] [0]) 
    
    return dp[0][1]
    
    
    
    
    
    
    
    
    
    