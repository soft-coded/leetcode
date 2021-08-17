class Solution:
    def trailingZeroes(self, n: int) -> int:
        five = 0
        while n != 0:
          temp = n // 5
          five += temp
          n //= 5
        return five