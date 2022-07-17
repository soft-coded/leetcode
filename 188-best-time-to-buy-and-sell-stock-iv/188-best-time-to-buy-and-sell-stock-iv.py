class Solution:
  def maxProfit(self, total: int, prices: List[int]) -> int:
    n = len(prices)
    total *= 2
    memo = {}
    def recur(i, k):
      if i == n or k > total:
        return 0
      memo_str = f"{i},{k}"
      if memo_str in memo:
        return memo[memo_str]
        
      if k & 1:
        # odd = sell
        memo[memo_str] = max(recur(i + 1, k + 1) + prices[i], recur(i + 1, k))                    
      else:
        # even = buy
        memo[memo_str] = max(recur(i + 1, k + 1) - prices[i], recur(i + 1, k))
            
      return memo[memo_str]
    
    return recur(0, 0)