class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      d = {}
      for i in range(len(strs)):
        srt = "".join(sorted(strs[i]))
        if srt not in d:
          d[srt] = []
        d[srt].append(strs[i])
      return d.values()