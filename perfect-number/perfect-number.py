class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False
        s = {1}
        i = 2
        while i <= num ** 0.5:
          if num % i == 0:
            s.add(i)
            s.add(num // i)
          i += 1
        return sum(s) == num
          