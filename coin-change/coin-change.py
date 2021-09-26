class Solution:
    def coinChange(self, cns: List[int], amt: int) -> int:
      if amt == 0: return 0
      dp = [-1] * amt
      for item in cns:
        if item <= amt:
          dp[item - 1] = 1
      for i in range(amt):
        if dp[i] == 1: continue
        mn = math.inf
        for item in cns:
          if i >= item and dp[i - item] != -1:
            mn = min(mn, dp[i - item])
        if mn != math.inf:
          dp[i] = mn + 1
      return dp[-1]