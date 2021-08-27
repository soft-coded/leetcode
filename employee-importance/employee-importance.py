"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, em: List['Employee'], idd: int) -> int:
      d = {}
      for item in em:
        d[item.id] = item
      ans = d[idd].importance
      dq = deque()
      for item in d[idd].subordinates:
        dq.append(item)
      while dq:
        item = dq.popleft()
        ans += d[item].importance
        for n in d[item].subordinates:
          dq.append(n)
      return ans