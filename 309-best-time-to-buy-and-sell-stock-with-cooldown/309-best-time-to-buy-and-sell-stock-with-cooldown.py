class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    memo = {}
    def recur(i, can_buy):
      if i >= n:
        return 0
      memo_str = "{},{}".format(i, can_buy)
      if memo_str in memo:
        return memo[memo_str]
        
      if not can_buy:
        memo[memo_str] = max(recur(i + 2, True) + prices[i], recur(i + 1, False))                    
      else:
        memo[memo_str] = max(recur(i + 1, False) - prices[i], recur(i + 1, True))
            
      return memo[memo_str]
    
    return recur(0, True)  