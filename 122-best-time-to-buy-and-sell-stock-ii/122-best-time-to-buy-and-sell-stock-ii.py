class Solution:
  def maxProfit(self, values: List[int]) -> int:
    n = len(values)
#     memo = {}
#     def recur(i, can_buy):
#       if i == n:
#         return 0
#       memo_str = "{},{}".format(i, can_buy)
#       if memo_str in memo:
#         return memo[memo_str]

#       if can_buy:
#         buy = recur(i + 1, False) - values[i]
#         dont_buy = recur(i + 1, True)
#         memo[memo_str] = max(buy, dont_buy)
#       else:
#         sell = recur(i + 1, True) + values[i]
#         dont_sell = recur(i + 1, False)
#         memo[memo_str] = max(sell, dont_sell)

#       return memo[memo_str]
    
#     return recur(0, True)

    # dp = [[0] * 2 for _ in range(n + 1)]
    # prev, cur = [0, 0], [0, 0]
    prev = [0, 0]
    
    for i in range(n - 1, -1, -1):
      for can_buy in range(2):
        if can_buy:
          buy = prev[0] - values[i]
          dont_buy = prev[1]
          # cur[can_buy] = max(buy, dont_buy)
          prev[can_buy] = max(buy, dont_buy)
        else:
          sell = prev[1] + values[i]
          dont_sell = prev[0]
          # cur[can_buy] = max(sell, dont_sell)
          prev[can_buy] = max(sell, dont_sell)
      
      # prev = cur
    
    return prev[1]
    
    
    
    