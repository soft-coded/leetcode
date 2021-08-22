class Solution:
    def findComplement(self, num: int) -> int:
      inv = ~0
      while inv & num: inv <<= 1
      return ~inv ^ num