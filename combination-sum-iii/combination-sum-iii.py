class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
      nums = list(range(1, 10))
      ans = []
      self.bt(k, n, ans, nums, [])
      return ans
    
    def bt(self, k, n, ans, nums, path):
      if n < 0: return
      if k == 0 and n == 0:
        ans.append(path)
        return
      
      for i in range(len(nums)):
        self.bt(k - 1, n - nums[i], ans, nums[i+1:], path + [nums[i]])