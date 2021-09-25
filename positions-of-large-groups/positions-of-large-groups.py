class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
      ans = []
      st = 0
      for i in range(1, len(s)):
        if s[i] != s[i - 1]:
          if i - st > 2:
            ans.append([st, i - 1])
          st = i
      if len(s) - st > 2:
        ans.append([st, len(s) - 1])
      return ans
          