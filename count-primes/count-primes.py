class Solution:
    def countPrimes(self, n: int) -> int:
        np = [False] * n
        cnt = 0
        for i in range(2, int(n ** 0.5) + 1):
          if not np[i]:
            j = 2
            while i * j < n:
              np[i * j] = True
              j += 1
        for i in range(2, n):
          if not np[i]: cnt += 1
        return cnt