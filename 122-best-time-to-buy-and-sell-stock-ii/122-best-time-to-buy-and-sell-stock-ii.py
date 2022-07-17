class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    memo = {}
    n = len(prices)
    def recur(i, can_buy):
      if i >= n:
        return 0
      memo_str = "{},{}".format(i, can_buy)
      if memo_str in memo:
        return memo[memo_str]
        
      if can_buy:
        memo[memo_str] = max(recur(i + 1, True), recur(i + 1, False) - prices[i])
      else:
        memo[memo_str] = max(recur(i + 1, False), recur(i + 1, True) + prices[i])
        
      return memo[memo_str]
    
    return recur(0, True)