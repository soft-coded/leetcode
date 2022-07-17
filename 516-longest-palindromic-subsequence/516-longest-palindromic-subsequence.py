class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
      memo = {}
      def recur(st, end):
        if st == end:
          return 1
        if st > end:
          return 0
        memo_str = f"{st},{end}"
        if memo_str in memo:
          return memo[memo_str]
        
        if s[st] == s[end]:
          memo[memo_str] = recur(st + 1, end - 1) + 2
        else:
          memo[memo_str] = max(recur(st + 1, end), recur(st, end - 1))
        
        return memo[memo_str]
      
      return recur(0, len(s) - 1)