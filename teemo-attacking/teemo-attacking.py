class Solution:
    def findPoisonedDuration(self, ts: List[int], d: int) -> int:
      ans = 0
      for i in range(len(ts) - 1):
        if ts[i + 1] <= ts[i] + d - 1:
          ans += ts[i + 1] - ts[i]
        else: ans += d
      ans += d
      return ans