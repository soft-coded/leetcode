class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
      odd = []
      even = []
      for item in nums:
        if item & 1:
          odd.append(item)
        else: even.append(item)
      return even + odd