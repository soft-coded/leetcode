class Solution:
    def longestPalindrome(self, s: str) -> str:
      if len(s) == 1:
        return s
      mx = 1
      ind = [0, 0]
      n = len(s)
      for i in range(n - 1):
        if s[i] == s[i + 1]:
          left = i - 1
          right = i + 2
          curlen = 2
          while left >= 0 and right < n and s[left] == s[right]:
            curlen += 2
            left -= 1
            right += 1
          if curlen > mx:
            mx = curlen
            ind[0] = left + 1
            ind[1] = right - 1
        
        if i > 0 and s[i - 1] == s[i + 1]:
          left = i - 2
          right = i + 2
          curlen = 3
          while left >= 0 and right < n and s[left] == s[right]:
            curlen += 2
            left -= 1
            right += 1
          if curlen > mx:
            mx = curlen
            ind[0] = left + 1
            ind[1] = right - 1
      
      return s[ind[0]: ind[1] + 1]
          