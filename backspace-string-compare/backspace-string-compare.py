class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      st1 = []
      st2 = []
      for item in s:
        if item == '#':
          if not st1: continue
          st1.pop()
        else:
          st1.append(item)
      for item in t:
        if item == '#':
          if not st2: continue
          st2.pop()
        else:
          st2.append(item)
      return st1 == st2