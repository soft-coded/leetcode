class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
      i = j = 0
      prev = ""
      while i < len(name):
        if j >= len(typed): return False
        if typed[j] == name[i]:
          prev = name[i]
          j += 1
          i += 1
        elif typed[j] == prev:
          j += 1
        else: return False
      while j < len(typed) and typed[j] == prev:
        j += 1
      return j == len(typed)