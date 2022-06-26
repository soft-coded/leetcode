class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      d = {}
      chars = set()
      for i in range(len(s)):
        if s[i] in d:
          if t[i] != d[s[i]]:
            return False
        else:
          if t[i] in chars:
            return False
          d[s[i]] = t[i]
          chars.add(t[i])
      return True