class Solution:
    def calPoints(self, ops: List[str]) -> int:
      sc = []
      for item in ops:
        if item == '+':
          sc.append(sc[-1] + sc[-2])
        elif item == 'D':
          sc.append(sc[-1] * 2)
        elif item == 'C':
          sc.pop()
        else:
          sc.append(int(item))
      return sum(sc)