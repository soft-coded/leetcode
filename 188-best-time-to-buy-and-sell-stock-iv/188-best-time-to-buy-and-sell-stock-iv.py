class Solution:
  def maxProfit(self, total: int, prices: List[int]) -> int:
    n = len(prices)
    total *= 2
#     memo = {}
#     def recur(i, k):
#       if i == n or k > total:
#         return 0
#       memo_str = f"{i},{k}"
#       if memo_str in memo:
#         return memo[memo_str]
        
#       if k & 1:
#         # odd = sell
#         memo[memo_str] = max(recur(i + 1, k + 1) + prices[i], recur(i + 1, k))                    
#       else:
#         # even = buy
#         memo[memo_str] = max(recur(i + 1, k + 1) - prices[i], recur(i + 1, k))
            
#       return memo[memo_str]
    
#     return recur(0, 0)

    dp = [[0] * (total + 1) for _ in range(n + 1)]
  
    for i in range(n - 1, -1, -1):
      for k in range(total - 1, -1, -1):
        if k & 1:
          # odd = sell
          dp[i][k] = max(dp[i + 1][k + 1] + prices[i], dp[i + 1][k])                   
        else:
          # even = buy
          dp[i][k] = max(dp[i + 1][k + 1] - prices[i], dp[i + 1][k])
          
    return dp[0][0]
          
  
  
  
  
  
  
  
  
  
  
  
  