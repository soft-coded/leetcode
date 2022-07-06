class Solution:
    def combinationSum(self, nums: List[int], target: int):
      ans = []
      
      def bt(nums, t, cur, ind):
        if t == 0:
          ans.append(cur)
          return
        if t < 0:
          return
        
        for i in range(ind, len(nums)):
          bt(nums, t - nums[i], cur + [nums[i]], i)
      
      bt(nums, target, [], 0)
      return ans