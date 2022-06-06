class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = {0: 0, 1: 0, 2: 0}
        for item in nums:
          d[item] += 1
        for i in range(len(nums)):
          if d[0]:
            nums[i] = 0
            d[0] -= 1
          elif d[1]:
            nums[i] = 1
            d[1] -= 1
          else:
            nums[i] = 2
        