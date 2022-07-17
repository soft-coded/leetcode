class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    memo = {}
    def recur(i, can_buy, total):
      if i >= n or total == 2:
        return 0
      memo_str = f"{i},{can_buy},{total}"
      if memo_str in memo:
        return memo[memo_str]
        
        
      if can_buy:
        memo[memo_str] = max(recur(i + 1, False, total + 0.5) - prices[i], recur(i + 1, True, total))
        
      else:
        memo[memo_str] = max(recur(i + 1, True, total + 0.5) + prices[i], recur(i + 1, False, total))
        
      return memo[memo_str]
        
    return recur(0, True, 0)