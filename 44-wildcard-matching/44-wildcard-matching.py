class Solution:
  def isMatch(self, text: str, pattern: str) -> bool:
      memo = {}
      def recur(i, j):
        if i < 0 and j < 0:
          return True
        if j < 0:
          for k in range(i + 1):
            if pattern[k] != '*':
              return False
          return True
        if i < 0:
          return False
        memo_str = f"{i},{j}"
        if memo_str in memo:
          return memo[memo_str]
        
        if pattern[i] == text[j] or pattern[i] == '?':
          memo[memo_str] = recur(i - 1, j - 1)
        elif pattern[i] == '*':
          memo[memo_str] = recur(i - 1, j) or recur(i, j - 1)
        else:
          memo[memo_str] = False
          
        return memo[memo_str]
        
      return recur(len(pattern) - 1, len(text) - 1)   