class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
      c = Counter(nums)
      ans = []
      for key, val in c.items():
        if val == 1:
          ans.append(key)
          if len(ans) == 2: break
      return ans