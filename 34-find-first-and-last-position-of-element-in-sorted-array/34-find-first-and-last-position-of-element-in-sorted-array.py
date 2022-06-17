class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
      left = bisect_left(nums, t)
      right = bisect_right(nums, t)
      ans = [-1, -1]
      if left == right:
        return ans
      if nums[left] == t:
        ans[0] = left
      if nums[right - 1] == t:
        ans[1] = right - 1
      return ans