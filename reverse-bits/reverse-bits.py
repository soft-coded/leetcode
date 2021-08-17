class Solution:
    def reverseBits(self, n: int) -> int:
        n = list(bin(n))
        n = n[len(n):1:-1]
        if len(n) < 32:
          n.extend(['0'] * (32 - len(n)))
        n = ''.join(n)
        return int(n, 2)