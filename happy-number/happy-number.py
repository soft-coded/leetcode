class Solution:
    def isHappy(self, n: int) -> bool:
      def get_next(n):
        sm = 0
        while n > 0:
            n, digit = divmod(n, 10)
            sm += digit ** 2
        return sm

      s = set()
      while n != 1 and n not in s:
          s.add(n)
          n = get_next(n)

      return n == 1