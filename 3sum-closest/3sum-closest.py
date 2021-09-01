class Solution:
    def threeSumClosest(self, nums: List[int], t: int) -> int:
      nums.sort()
      ans = nums[0] + nums[1] + nums[2]
      for i in range(len(nums)-2):
          l, r = i + 1, len(nums) - 1
          while l < r:
              s = nums[i] + nums[l] + nums[r]
              if s == t: return t
              if abs(t - s) < abs(t - ans): ans = s
              if s < t: l += 1 
              else : r -= 1
      return ans