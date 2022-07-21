class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      mx = start = 0
      d = {}
      for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
          mx = max(mx, i - start)
          start = d[s[i]] + 1
        d[s[i]] = i
      return max(mx, len(s) - start)