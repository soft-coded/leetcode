class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      mx = 0
      cur = 0
      for i in range(len(nums)):
        if nums[i] == 1:
          cur += 1
        elif nums[i] == 0:
          mx = max(mx, cur)
          cur = 0
      mx = max(mx, cur)
      return mx
        