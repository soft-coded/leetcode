class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      n = len(text1) + 1
      m = len(text2) + 1
      dp = [[0] * m for _ in range(n)]
      for i in range(n - 1):
        for j in range(m - 1):
          if text1[i] == text2[j]:
            dp[i + 1][j + 1] = 1 + dp[i][j]
          else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
      return dp[n - 1][m - 1]