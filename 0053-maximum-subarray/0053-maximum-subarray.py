class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_here = max_all = nums[0]
    for i in range(1, len(nums)):
      max_here = max(max_here + nums[i], nums[i])
      max_all = max(max_all, max_here)
    
    return max_all