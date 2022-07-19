class Solution(object):
  def subsetsWithDup(self, nums):
    ans = []
    def bt(nums, path, ans, ind):
      ans.append(path)
      
      for i in range(ind, len(nums)):
        if i > ind and nums[i] == nums[i - 1]: 
          continue
        bt(nums, path + [nums[i]], ans, i + 1)
    
    bt(sorted(nums), [], ans, 0)
    return ans
        