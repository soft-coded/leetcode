class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
      d = {}
      ans = 2001
      res = []
      for i in range(len(l1)):
        d[l1[i]] = i
      for i in range(len(l2)):
        ind = d.get(l2[i])
        if ind is not None and i + ind < ans:
          ans = i + ind
      for i in range(len(l2)):
        ind = d.get(l2[i])
        if ind is not None and i + ind == ans:
          res.append(l2[i])
      return res