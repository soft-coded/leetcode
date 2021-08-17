from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        n = len(nums)
        for key, val in cntr.items():
          if val > n // 2: return key