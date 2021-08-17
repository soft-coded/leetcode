class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for item in nums:
          d[item] = d.get(item, 0) + 1
        for key, val in d.items():
          if val == 1: return key