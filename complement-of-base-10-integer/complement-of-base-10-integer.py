class Solution:
    def bitwiseComplement(self, n: int) -> int:
      ans = ""
      for item in bin(n)[2:]:
        if item == '1':
          ans += '0'
        else: ans += '1'
      return int(ans, 2)