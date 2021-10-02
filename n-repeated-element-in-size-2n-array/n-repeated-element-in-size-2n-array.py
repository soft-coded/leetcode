class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
      s = set()
      for item in nums:
        if item in s: 
          return item
        s.add(item)