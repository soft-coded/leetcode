class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','')
        n = len(s)
        i = n % k
        ans = s[:i] + '-' if i else ""
        n //= k
        while n:
          ans += s[i:i + k] + '-'
          i += k
          n -= 1
        return ans.upper()[:len(ans) - 1]
        