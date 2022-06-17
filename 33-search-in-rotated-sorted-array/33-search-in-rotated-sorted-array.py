class Solution:
    def search(self, nums: List[int], t: int) -> int:
      lo, hi = 0, len(nums) - 1
      while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == t:
          return mid
        if nums[lo] <= nums[mid]:
          if nums[lo] <= t < nums[mid]:
            hi = mid - 1
          else:
            lo = mid + 1
        else:
          if nums[mid] < t <= nums[hi]:
            lo = mid + 1
          else:
            hi = mid - 1
      return -1