class Solution(object):
    def subsetsWithDup(self, nums):
        ret = []
        self.bt(sorted(nums), [], ret)
        return ret
    
    def bt(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            self.bt(nums[i+1:], path+[nums[i]], ret)
        