class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
      flat = []
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          flat.append(grid[i][j])
      k %= len(flat)
      flat = flat[-k:] + flat[:-k]
      ind = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          grid[i][j] = flat[ind]
          ind += 1
      return grid