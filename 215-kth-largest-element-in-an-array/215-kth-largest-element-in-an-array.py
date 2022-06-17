def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      k = len(nums) - k
      st = 0
      end = len(nums) - 1
      while True:
        pivot = nums[st]
        left = st + 1
        right = end
        while left <= right:
          if nums[left] > pivot and nums[right] < pivot:
            swap(nums, left, right)
          if nums[left] <= pivot:
            left += 1
          if nums[right] >= pivot:
            right -= 1
        swap(nums, st, right)
        if right == k:
          return nums[right]
        if k < right:
          end = right - 1
        else:
          st = right + 1