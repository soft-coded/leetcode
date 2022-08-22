class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
      return (goal ^ start).bit_count()