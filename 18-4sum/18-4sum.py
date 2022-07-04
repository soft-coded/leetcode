class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
      nums.sort()
      n = len(nums)
      i = 0
      ans = []
      while i < n:
        j = i + 1
        while j < n:
          left = j + 1
          right = n - 1
          t = target - nums[i] - nums[j]
          while left < right:
            sm = nums[left] + nums[right]
            if sm == t:
              ans.append([nums[i], nums[j], nums[left], nums[right]])
              while left < right and nums[left] == nums[left + 1]:
                left += 1
              while right > left and nums[right] == nums[right - 1]:
                right -= 1
              left += 1
              right -= 1
            elif t > sm:
              left += 1
            else:
              right -= 1
          while j < n - 1 and nums[j] == nums[j + 1]:
            j += 1
          j += 1
        while i < n - 1 and nums[i] == nums[i + 1]:
          i += 1
        i += 1
      
      return ans
            