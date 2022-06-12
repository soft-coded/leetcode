class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
      if len(nums) == 1:
        return 0
      
      mx = -math.inf
      mn = math.inf
      inds = [-1, -1]
      for i in range(len(nums)):
        if self.out_of_order(nums, i):
          mx = max(mx, nums[i])
          mn = min(mn, nums[i])
      
      if mn == math.inf:
        return 0
      
      i = 0
      while mn >= nums[i]:
        i += 1
      inds[0] = i
      
      i = len(nums) - 1
      while mx <= nums[i]:
        i -= 1
      inds[1] = i + 1
      return inds[1] - inds[0]
    
    def out_of_order(self, nums, i):
      if i == 0:
        return nums[i] > nums[i + 1]
      if i == len(nums) - 1:
        return nums[i] < nums[i - 1]
      return nums[i] > nums[i + 1] or nums[i] < nums[i - 1]