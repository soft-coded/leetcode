class Solution:
    def numDistinct(self, s: str, t: str) -> int:
      lt = len(t)
      ls = len(s)
      memo = {}
      def recur(i, j):
        if j < 0:
          return 1
        if i < 0:
          return 0
        memo_str = "{},{}".format(i, j)
        if memo_str in memo:
          return memo[memo_str]

        if s[i] == t[j]:
          memo[memo_str] = recur(i - 1, j - 1) + recur(i - 1, j)
        else:
          memo[memo_str] = recur(i - 1, j)
          
        return memo[memo_str]

      return recur(ls - 1, lt - 1)