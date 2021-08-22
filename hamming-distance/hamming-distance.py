class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0; n = x ^ y
        while n:
          if n & 1: cnt += 1
          n >>= 1
        return cnt