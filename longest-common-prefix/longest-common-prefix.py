class Solution:
    def find_prefix(self, s1, s2):
      n1, n2 = len(s1), len(s2)
      i = 0
      ans = ""
      while i < n1 and i < n2:
        if s1[i] != s2[i]: break
        ans += s1[i]
        i+=1
      return ans
      
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1, len(strs)):
          ans = self.find_prefix(ans, strs[i])
        return ans