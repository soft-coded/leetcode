class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ans = 0
        rmin = m
        cmin = n
        for item in ops:
          r, c = item
          rmin = min(r, rmin)
          cmin = min(c, cmin)
        return rmin * cmin