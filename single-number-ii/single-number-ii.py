class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      c = Counter(nums)
      for key, val in c.items():
        if val != 3: return key