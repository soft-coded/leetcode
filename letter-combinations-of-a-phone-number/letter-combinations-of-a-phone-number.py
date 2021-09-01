class Solution:
    def letterCombinations(self, s: str) -> List[str]:
      ans = deque()
      if not s: return ans
      d = [0, 1, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
      ans.append("")
      while len(ans[0]) != len(s):
        st = ans.popleft()
        mp = d[int(s[len(st)])]
        for item in mp:
          ans.append(st+item)
      return ans