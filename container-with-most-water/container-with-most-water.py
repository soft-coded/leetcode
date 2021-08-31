class Solution:
    def maxArea(self, h: List[int]) -> int:
      i, j = 0, len(h) - 1
      mx = 0
      while i < j:
        mx = max(mx, (j-i)*min(h[i], h[j]))
        if h[i] < h[j]:
          i += 1
        else:
          j -= 1
      return mx