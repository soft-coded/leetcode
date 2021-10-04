class Solution:
    def balancedStringSplit(self, s: str) -> int:
      r = l = cnt = 0
      for item in s:
        if item == 'L':
          l += 1
        elif item == 'R':
          r += 1
        if r == l:
          cnt += 1
      return cnt