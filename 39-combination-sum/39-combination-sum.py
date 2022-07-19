class Solution:
  def combinationSum(self, nums: List[int], target: int):
    ans = []
      
#       def bt(nums, t, cur, ind):
#         if t == 0:
#           ans.append(cur)
#           return
#         if t < 0:
#           return
        
#         for i in range(ind, len(nums)):
#           bt(nums, t - nums[i], cur + [nums[i]], i)
      
#       bt(nums, target, [], 0)
#       return ans

    def recur(i, cursum, path):
      if cursum == target:
        return ans.append(path)
      if i < 0:
        return
      
      # not_pick
      recur(i - 1, cursum, path)
      
      # pick
      sm = cursum + nums[i]
      if sm <= target:
        recur(i, sm, path + [nums[i]])
    
    recur(len(nums) - 1, 0, [])
    return ans     
      
      
      
      