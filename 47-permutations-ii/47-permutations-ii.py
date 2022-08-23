def swap(i, j, arr):
  arr[i], arr[j] = arr[j], arr[i]

class Solution:
  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    ans = []
    
    def bt(i):
      if i == len(nums) - 1:
        ans.append(nums[:])
        return
      
      s = set()
      
      for j in range(i, len(nums)):
        if nums[j] in s:
          continue
        
        swap(i, j, nums)
        bt(i + 1)
        swap(i, j, nums)
        s.add(nums[j])
    
    bt(0)
    return ans
        