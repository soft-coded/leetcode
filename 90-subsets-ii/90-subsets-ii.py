class Solution(object):
    def subsetsWithDup(self, nums):
        ans = []
        self.bt(sorted(nums), [], ans)
        return ans
    
    def bt(self, nums, path, ans):
        ans.append(path)
        for i in range(len(nums)):
          if i > 0 and nums[i] == nums[i - 1]: 
            continue
          self.bt(nums[i + 1:], path + [nums[i]], ans)
        