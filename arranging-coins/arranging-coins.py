class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while i * (i + 1) / 2 < n:
          i += 1
        return i - 1 if i * (i + 1) / 2 != n else i