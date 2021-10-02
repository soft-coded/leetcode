class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
      n = 0
      for item in num:
        n += item
        n *= 10
      n //= 10
      n += k
      return list(str(n))