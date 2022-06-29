class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> bool:
      st = set(wd)
      dp = [False] * (len(s) + 1)
      dp[0] = True
      for i in range(1, len(s) + 1):
        for j in range(i):
          if dp[j] and s[j:i] in st:
            dp[i] = True
            break
      return dp[-1]