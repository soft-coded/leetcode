class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      d = {}
      for i in range(1, n + 1):
        d[i] = set()
      for item in trust:
        d[item[0]].add(item[1])
      juj = None
      for key, val in d.items():
        if not val:
          juj = key
          break
      for key, val in d.items():
        if key != juj and juj not in val:
          return -1
      return juj