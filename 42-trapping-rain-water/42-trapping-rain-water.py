class Solution:
    def trap(self, h: List[int]) -> int:
      n = len(h)
      mxs = [0] * n
      # ans = 0
      left = right = 0
      
      for i in range(n):
        mxs[i] = left
        left = max(left, h[i])
      
      for i in range(n - 1, -1, -1):
        mnh = min(right, mxs[i])
        if h[i] < mnh:
          mxs[i] = mnh - h[i]
        else:
          mxs[i] = 0
        right = max(right, h[i])
      
      return sum(mxs)