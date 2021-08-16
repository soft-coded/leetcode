class Solution:
    def maxSubArray(self, a: List[int]) -> int:
      mx = a[0]
      mxn = a[0]
      for i in range(1,len(a)):
        mxn = max(a[i], mxn + a[i])
        mx = max(mx, mxn)
      return mx