class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
      ans = []
      cur = 0
      for item in nums:
        cur |= item
        ans.append(cur % 5 == 0)
        cur <<= 1
      return ans