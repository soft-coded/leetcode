class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
      l = bisect_left(nums, t)
      r = bisect_right(nums, t) - 1
      try:
        return [l if nums[l] == t else -1, r if nums[r] == t else -1]
      except:
        return [-1, -1]