class Solution:
    def permute(self, nums):
      ans = []
      self.dfs(nums, [], ans)
      return ans
    
    def dfs(self, nums, path, res):
      if not nums:
        res.append(path)
      for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)