class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      d = {}
      for item in strs:
        item_s = "".join(sorted(item))
        if item_s in d:
          d[item_s].append(item)
        else:
          d[item_s] = [item]
      return d.values()