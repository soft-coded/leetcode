class Solution:
    def judgeCircle(self, moves: str) -> bool:
      x = y = 0
      for item in moves:
        if item == 'L': x -= 1
        elif item == 'R': x += 1
        elif item == 'U': y += 1
        else: y -= 1
      return x == 0 and y == 0