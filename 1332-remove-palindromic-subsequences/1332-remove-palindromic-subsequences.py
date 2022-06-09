def is_palin(s):
  n = len(s) - 1
  for i in range(math.ceil(len(s) / 2)):
    if s[i] != s[n - i]:
      return False
  return True

class Solution:
    def removePalindromeSub(self, s: str) -> int:
      if is_palin(s): return 1
      return 2