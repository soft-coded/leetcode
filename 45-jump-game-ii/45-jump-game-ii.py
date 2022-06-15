class Solution:
    def jump(self, nums: List[int]) -> int:
      jmp = end = far = 0
      for i in range(len(nums) - 1):
        far = max(far, i+nums[i])
        if i == end:
          end = far
          jmp += 1
      return jmp