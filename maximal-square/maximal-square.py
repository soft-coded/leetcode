class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
      rows = len(matrix)
      cols = len(matrix[0])
      dp = [[0] * (cols + 1) for _ in range(rows + 1)]
      mx = 0
      for r in range(rows):
        for c in range(cols):
          if matrix[r][c] == '1':
            dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1
            mx = max(mx, dp[r + 1][c + 1])
      return mx * mx