def swap(arr, i, j):
  arr[i], arr[j] = arr[j], arr[i]

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    
    def bt(i):
      if i == len(nums) - 1:
        ans.append(nums[:])
        return
      
      for j in range(i, len(nums)):
        swap(nums, i, j)
        bt(i + 1)
        swap(nums, i, j)
    
    bt(0)
    return ans