class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
      c = Counter(text)
      cnt = 0
      while True:
        if c['b'] < 1 or c['a'] < 1 or c['l'] < 2 or c['o'] < 2 or c['n'] < 1:
          break
        cnt += 1
        c['b'] -= 1
        c['a'] -= 1
        c['l'] -= 2
        c['o'] -= 2
        c['n'] -= 1
      return cnt