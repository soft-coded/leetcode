class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i in range(len(nums)):
          if target - nums[i] in s:
            ind = nums.index(target - nums[i])
            if ind != i:
              return [i, ind]