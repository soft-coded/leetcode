class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      r = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
      ans = []
      for item in words:
        l = item.lower()
        f = True
        row = 0 if r[0].find(l[0]) >= 0 else -1
        if row < 0:
          row = 1 if r[1].find(l[0]) >= 0 else 2
        for c in l[1:]:
          if r[row].find(c) < 0:
            f = False
            break
        if f: ans.append(item)
      return ans