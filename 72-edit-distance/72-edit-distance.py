class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recur(i, j, memo):
          if i < 0 and j < 0:
            return 0
          if i < 0:
            return j + 1
          if j < 0:
            return i + 1
          
          memo_str = f"{i},{j}"
          if memo_str in memo:
            return memo[memo_str]
          
          if word1[i] == word2[j]:
            return recur(i - 1, j - 1, memo)
          
          ans = min(recur(i - 1, j, memo), recur(i, j - 1, memo), recur(i - 1, j - 1, memo)) + 1
          memo[memo_str] = ans
          return ans
        
        return recur(len(word1) - 1, len(word2) - 1, {})