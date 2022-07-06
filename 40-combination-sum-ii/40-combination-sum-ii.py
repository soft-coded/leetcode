class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def bt(nums, t, cur, ind):
          if t == 0:
            ans.append(cur)
            return
          if t < 0:
            return
          
          for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
              continue
            if nums[i] > t:
              break
            bt(nums, t - nums[i], cur + [nums[i]], i + 1)
        
        bt(nums, target, [], 0)
        return ans