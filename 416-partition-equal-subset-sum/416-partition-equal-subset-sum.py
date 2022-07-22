class Solution:
  def canPartition(self, nums: List[int]) -> bool:
#     total = sum(nums)
#     if total % 2:
#       return False
    
#     target = total // 2
#     memo = {}
#     def recur(i, t):
#       if t == 0:
#         return True
#       if i < 0 or t < 0:
#         return False
#       memo_str = f"{i},{t}"
#       if memo_str in memo:
#         return memo[memo_str]
      
#       not_pick = recur(i - 1, t)
#       pick = recur(i - 1, t - nums[i])
#       memo[memo_str] = pick or not_pick
#       return memo[memo_str]
    
#     return recur(len(nums) - 1, target)
    
    target, n = sum(nums), len(nums)
    if target & 1: return False
    target >>= 1
    dp = [True] + [False] * target
    for x in nums:
      dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
      if dp[target]: return True
    return False
  
  
  
  
  