class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    memo = {}
    def recur(i, j):
      if i == 0 and j == 0:
        return grid[0][0]
      if i < 0 or j < 0:
        return math.inf
      memo_str = f"{i},{j}"
      if memo_str in memo:
        return memo[memo_str]
      
      
      up = recur(i - 1, j)
      left = recur(i, j - 1)
      memo[memo_str] = min(up, left) + grid[i][j]
      return memo[memo_str]
    return recur(len(grid) - 1, len(grid[0]) - 1)