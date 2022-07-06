class Solution:
    def combinationSum(self, nums: List[int], target: int):
      ans = []
      
      def bt(nums, t, cur):
        if t == 0:
          ans.append(cur)
          return
        if t < 0:
          return
        
        for i in range(len(nums)):
          bt(nums[i:], t - nums[i], cur + [nums[i]])
      
      bt(nums, target, [])
      return ans