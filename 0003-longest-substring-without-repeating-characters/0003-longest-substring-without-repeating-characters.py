class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        d = {}
        ans = 0
        
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                ans = max(ans, i - start)
                start = d[s[i]] + 1
            d[s[i]] = i
        
        return max(ans, len(s) - start)