class Solution:
    def canJump(self, nums: List[int]) -> bool:
      far = i = 0
      while i < len(nums) and i <= far:
        far = max(far, i+nums[i])
        i += 1
      return i == len(nums)
      