def center(s, l, r):
  while l >= 0 and r < len(s) and s[l] == s[r]:
    l -=1
    r += 1
  return r - l - 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
      if not s: return s
      st = end = 0
      for i in range(len(s)):
        l1 = center(s, i, i)
        l2 = center(s, i, i + 1)
        l = max(l1, l2)
        if (l > end - st):
          st = i - (l - 1) // 2
          end = i + l // 2 
      return s[st:end+1]