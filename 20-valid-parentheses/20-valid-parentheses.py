class Solution:
    def isValid(self, s: str) -> bool:
      st = []
      d = {
        ']': '[',
        '}': '{',
        ')': '('
      }
      clos = "]})"
      for item in s:
        if item in clos:
          if not st or st[-1] != d[item]:
            return False
          st.pop()
        else:
          st.append(item)
      return len(st) == 0