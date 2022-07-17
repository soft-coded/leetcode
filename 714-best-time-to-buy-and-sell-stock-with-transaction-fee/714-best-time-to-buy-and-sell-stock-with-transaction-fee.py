class Solution:
  def maxProfit(self, prices: List[int], fee: int) -> int:
    n = len(prices)
    memo = {}
    def recur(i, can_buy):
      if i == n:
        return 0
      memo_str = f"{i},{can_buy}"
      if memo_str in memo:
        return memo[memo_str]
        
      if can_buy:
        memo[memo_str] = max(recur(i + 1, False) - prices[i], recur(i + 1, True))
      else:
        memo[memo_str] = max(recur(i + 1, True) + prices[i] - fee, recur(i + 1, False))
      return memo[memo_str]
        
    return recur(0, True)  