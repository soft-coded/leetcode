class Solution:
    def trap(self, h: List[int]) -> int:
      n = len(h)
      left = [0] * n
      left[0] = h[0]
      right = [0] * n
      right[-1] = h[-1]
      ans = 0
      
      for i in range(1, n):
        left[i] = max(left[i - 1], h[i])
      
      for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], h[i])

      for i in range(n):
        mn = min(left[i], right[i])
        if h[i] < mn:
          ans += mn - h[i]
      
      return ans