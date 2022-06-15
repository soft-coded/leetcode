class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
      n = len(s1) + 1
      m = len(s2) + 1
      dp = [[0 for _ in range(m)] for _ in range(n)]
      for i in range(1, n):
        for j in range(1, m):
          if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
          else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
      return dp[-1][-1]