class Solution:
    def maxProduct(self, nums: List[int]) -> int:
      mx = mn = ans = nums[0]
      for item in nums[1:]:
        if item < 0: 
          mx, mn = mn, mx
        mx = max(item, mx * item)
        mn = min(item, mn * item)
        ans = max(ans, mx)
      return ans