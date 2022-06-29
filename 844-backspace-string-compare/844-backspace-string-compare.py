class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      st1 = []
      st2 = []
      for char in s:
        if char == '#':
          if st1:
            st1.pop()
        else:
          st1.append(char)
      
      for char in t:
        if char == '#':
          if st2:
            st2.pop()
        else:
          st2.append(char)
      
      return st1 == st2