class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      mx = prev = 0
      d = {}
      for i in range(len(s)):
        if s[i] in d and d[s[i]] >= prev:
          mx = max(mx, i - prev)
          prev = d[s[i]] + 1
        d[s[i]] = i
      return max(mx, len(s) - prev)