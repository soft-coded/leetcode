class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        ans = []
        n = num < 0
        num = abs(num)
        while num:
          ans.append(str(num % 7))
          num //= 7
        if n: ans.append('-')
        ans.reverse()
        return ''.join(ans)