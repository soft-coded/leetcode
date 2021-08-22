class Solution:
    def findComplement(self, num: int) -> int:
        n = list(bin(num)[2:])
        for i in range(len(n)):
          n[i] = '1' if n[i] == '0' else '0'
        return int(''.join(n), 2)