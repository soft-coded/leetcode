class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 100001
        profit = 0
        for item in prices:
          if item < mn: mn = item
          elif item - mn > profit:
            profit = item - mn
        return profit