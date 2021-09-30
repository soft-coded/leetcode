class Solution:
    def integerReplacement(self, n: int) -> int:
      self.vis = {}
      return self.recur(n)
    
    def recur(self, n):
      if n == 1: return 0
      if n not in self.vis:
        if n & 1:
          self.vis[n] = 2 + min(self.recur(n // 2), self.recur(n // 2 + 1))
        else:
          self.vis[n] = 1 + self.recur(n // 2)
      return self.vis[n]