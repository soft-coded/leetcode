from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for val in c.values():
          if val > 1: return True
        return False