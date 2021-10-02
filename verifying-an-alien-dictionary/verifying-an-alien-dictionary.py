class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
      if len(words) == 1: return True
      d = {}
      i = 0
      for item in order:
        d[item] = i
        i += 1
      for i in range(1, len(words)):
        prev = words[i - 1]
        nxt = words[i]
        for j in range(len(prev)):
          if j >= len(nxt): 
            return False
          if d[prev[j]] < d[nxt[j]]:
            break
          if d[prev[j]] > d[nxt[j]]:
            return False
      return True