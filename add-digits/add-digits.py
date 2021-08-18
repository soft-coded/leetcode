class Solution:
    def addDigits(self, num: int) -> int:
        def divide(n):
          sm = 0
          while n:
            sm += n % 10
            n //= 10
          return sm
        while num // 10:
          num = divide(num)
        return num