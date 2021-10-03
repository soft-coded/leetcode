class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
      ans = 0
      c = Counter(chars)
      for item in words:
        f = False
        tc = c.copy()
        for ch in item:
          if tc[ch] == 0:
            f = True
            break
          tc[ch] -= 1
        if not f: ans += len(item)
      return ans