class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      n = len(nums)
      ans = [[]]
      for item in nums:
          ans += [cur + [item] for cur in ans]
      return ans
      