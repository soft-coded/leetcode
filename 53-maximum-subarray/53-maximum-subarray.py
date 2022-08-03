class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_all = max_here = nums[0]
    for i in range(1, len(nums)):
      max_here = max(max_here + nums[i], nums[i])
      max_all = max(max_here, max_all)
    return max_all