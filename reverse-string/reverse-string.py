class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        i = 0
        while i < n // 2:
          temp = s[i]
          s[i] = s[n - i - 1]
          s[n - i - 1] = temp
          i += 1
        