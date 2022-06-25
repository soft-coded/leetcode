class Solution:
    def tribonacci(self, n: int) -> int:
      f = 0
      s = t = 1
      cur = None
      while n:
        cur = f + s + t
        f = s
        s = t
        t = cur
        n -= 1
      return f