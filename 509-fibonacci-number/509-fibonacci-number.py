class Solution:
    def fib(self, n: int) -> int:
      first = 0
      second = 1
      cur = None
      while n:
        cur = first + second
        first = second
        second = cur
        n -= 1
      return first