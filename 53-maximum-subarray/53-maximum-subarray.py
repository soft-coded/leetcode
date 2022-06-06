class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      cur = mx = -math.inf
      for item in nums:
        cur = max(cur + item, item)
        mx = max(mx, cur)
      return mx