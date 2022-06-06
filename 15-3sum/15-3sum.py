class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      ans = set()
      nums.sort()
      n = len(nums)
      for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
          sm = nums[i] + nums[left] + nums[right]
          if sm == 0:
            ans.add((nums[i], nums[left], nums[right]))
            while left < right and nums[right] == nums[right - 1]: right -= 1
            while left < right and nums[left] == nums[left + 1]: left += 1
            left += 1
            right -= 1
          elif sm > 0:
            right -= 1
          else:
            left += 1
      return ans