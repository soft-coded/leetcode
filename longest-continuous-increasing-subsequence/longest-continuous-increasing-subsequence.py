class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
      mx = 1
      cur = 1
      for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
          mx = max(mx, cur)
          cur = 1
        else:
          cur += 1
      mx = max(mx, cur)
      return mx