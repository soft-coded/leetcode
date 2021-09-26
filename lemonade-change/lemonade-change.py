class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
      d = {5: 0, 10: 0}
      for item in bills:
        if item == 20:
          if d[10] and d[5]:
            d[10] -= 1
            d[5] -= 1
          elif d[5] > 2:
            d[5] -= 3
          else: return False
        elif item == 10:
          if d[5]:
            d[5] -= 1
            d[10] += 1
          else: return False
        else: d[5] += 1
      return True