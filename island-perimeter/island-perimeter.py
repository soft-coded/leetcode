class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        p = 0
        n = len(g)
        for i in range(n):
          m = len(g[i])
          for j in range(m):
            if g[i][j] == 1:
              add = 0
              if i == 0 or (i > 0 and g[i - 1][j] == 0): 
                add += 1
              if i == n - 1 or (i < n - 1 and g[i + 1][j] == 0):
                add += 1
              if j == 0 or (j > 0 and g[i][j - 1] == 0):
                add += 1
              if j == m - 1 or (j < m - 1 and g[i][j + 1] == 0):
                add += 1
              p += add
        return p