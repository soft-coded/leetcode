class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
      intv.sort()
      ans = []
      lo = intv[0][0]
      hi = intv[0][1]
      for i in range(1, len(intv)):
        if hi >= intv[i][0]:
          hi = max(intv[i][1], hi)
        else:
          ans.append([lo, hi])
          lo = intv[i][0]
          hi = intv[i][1]
      ans.append([lo, hi])
      return ans