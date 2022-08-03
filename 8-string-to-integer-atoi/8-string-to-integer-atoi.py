class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s: return 0
        neg = False
        if s[0] == '+': s = s[1:]
        elif s[0] == '-': 
          neg = True
          s = s[1:]
        i = 0
        ans = 0
        while i < len(s) and s[i].isdigit():
          ans += int(s[i])
          ans *= 10
          i += 1
        ans = -ans // 10 if neg else ans // 10
        if ans < -2147483648: ans = -2147483648
        elif ans > 2147483647: ans = 2147483647
        return ans