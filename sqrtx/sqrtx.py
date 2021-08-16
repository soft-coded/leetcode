class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        root = 0
        for i in range(1, x):
          if i*i <= x: root = i
          else: break
        return root