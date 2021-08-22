class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for item in collections.Counter(s).values():
          ans += item // 2 * 2
        if ans < len(s): ans += 1
        return ans