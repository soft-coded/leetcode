import string

class Solution:
    def convertToTitle(self, num: int) -> str:
        res = []
        asc = ord('A')
        while num:
          res.append(string.ascii_uppercase[(num - 1) % 26])
          num = (num - 1) // 26
        res.reverse()
        return ''.join(res)