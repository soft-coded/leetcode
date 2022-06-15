class Solution:
    def jump(self, nums: List[int]) -> int:
      if len(nums) == 1: return 0
      mx_reach = steps = nums[0]
      jumps = 0
      for i in range(1, len(nums) - 1):
        mx_reach = max(mx_reach, i + nums[i])
        steps -= 1
        if steps == 0:
          jumps += 1
          steps = mx_reach - i
      return jumps + 1