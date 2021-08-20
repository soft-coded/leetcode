from collections import Counter

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        dr = Counter(r)
        dm = Counter(m)
        for key, val in dr.items():
          if not dm.get(key) or dm[key] < val: return False
        return True