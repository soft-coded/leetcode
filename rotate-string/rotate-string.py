class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
      d = {}
      for i in range(len(s)):
        if s[i] not in d:
          d[s[i]] = []
        d[s[i]].append(i)
      try:
        for ind in d[goal[0]]:
          if goal == s[ind:] + s[:ind]:
            return True
        return False
      except:
        return False