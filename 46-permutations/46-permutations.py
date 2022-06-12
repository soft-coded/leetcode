def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      ans = []
      self.backtrack(nums, ans, 0)
      return ans
    
    def backtrack(self, nums, ans, i):
      if i == len(nums) - 1:
        ans.append(nums[:])
        return

      for j in range(i, len(nums)):
        swap(nums, i, j)
        self.backtrack(nums, ans, i + 1)
        swap(nums, i, j)