class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    mx = mn = ans = nums[0]
    for i in range(1, len(nums)):
      if nums[i] < 0:
        mx, mn = mn, mx
      
      mx = max(mx * nums[i], nums[i])
      mn = min(mn * nums[i], nums[i])
      ans = max(ans, mx)
    
    return ans