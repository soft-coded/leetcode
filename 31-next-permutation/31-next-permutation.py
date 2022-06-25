def reverse(st, end, arr):
  while st < end:
    arr[st], arr[end] = arr[end], arr[st]
    st += 1
    end -= 1

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
      n = len(nums)
      i = n - 2
      while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
      
      if i >= 0:
        j = n - 1
        while nums[i] >= nums[j]:
          j -= 1
        
        nums[j], nums[i] = nums[i], nums[j]
      
      reverse(i + 1, n - 1, nums)
      
      return nums