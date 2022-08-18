class Solution:
  def maxProfit(self, values: List[int]) -> int:
    n = len(values)
    memo = {}
    def recur(i, can_buy):
      if i == n:
        return 0
      memo_str = "{},{}".format(i, can_buy)
      if memo_str in memo:
        return memo[memo_str]

      if can_buy:
        buy = recur(i + 1, False) - values[i]
        dont_buy = recur(i + 1, True)
        memo[memo_str] = max(buy, dont_buy)
      else:
        sell = recur(i + 1, True) + values[i]
        dont_sell = recur(i + 1, False)
        memo[memo_str] = max(sell, dont_sell)

      return memo[memo_str]
    
    return recur(0, True)