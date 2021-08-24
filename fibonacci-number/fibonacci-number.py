class Solution:
    def fib(self, n: int) -> int:
      if n == 0: return n
      a = 0
      b = 1
      i = 1
      while i < n:
        temp = b
        b = a + b
        a = temp
        i += 1
      return b