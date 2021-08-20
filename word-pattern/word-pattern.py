class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(p) or len(set(s)) != len(set(p)): return False
        d = {}
        for i in range(len(p)):
          if d.get(p[i]) is None: d[p[i]] = []
          d[p[i]].append(i)
        for val in d.values():
          ind = val[0]
          for i in range(1, len(val)):
            if s[val[i]] != s[ind]:
              return False
        return True
            
        