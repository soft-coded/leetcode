class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
      b = bin(n)
      for i in range(1, len(b)):
        if b[i - 1] == b[i]: return False
      return True