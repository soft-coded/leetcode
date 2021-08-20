class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for item in s:
          ind = t.find(item, i)
          if ind < 0: return False
          i = ind + 1
        return True