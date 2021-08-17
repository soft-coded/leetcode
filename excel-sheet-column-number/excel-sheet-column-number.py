class Solution:
    def titleToNumber(self, tit: str) -> int:
        num = 0
        tit = tit[::-1]
        asc = ord('A')
        for i in range(len(tit)):
          num += (ord(tit[i]) - asc + 1) * 26 ** i
        return num