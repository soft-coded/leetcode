# def is_palin(s, st, end):
#   while st < end:
#     if s[st] != s[end]:
#       return False
#     st += 1
#     end -= 1
#   return True

# class Solution:
#   def minCut(self, s: str) -> int:
#     memo = {}
#     def recur(i):
#       if i == len(s):
#         return 0
#       if i in memo:
#         return memo[i]
        
#       memo[i] = math.inf
#       for j in range(i, len(s)):
#         if is_palin(s, i, j):
#           memo[i] = min(memo[i], recur(j + 1) + 1)
        
#       return memo[i]
    
#     return recur(0) - 1

#     n = len(s)
#     dp = [0] * (n + 1)

#     for i in range(n - 1, -1, -1):
#       dp[i] = math.inf
#       for j in range(i, len(s)):
#         if is_palin(s, i, j):
#           dp[i] = min(dp[i], dp[j + 1] + 1)
        
#     return dp[0] - 1
      
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        @lru_cache(None)
        def is_palin(l, r):
            if l >= r: 
              return True
            if s[l] != s[r]: 
              return False
            return is_palin(l + 1, r - 1)
        
        @lru_cache(None)
        def recur(i):
            if i == n:
                return 0
              
            ans = math.inf
            for j in range(i, n):
                if is_palin(i, j):
                    ans = min(ans, recur(j + 1) + 1)
            return ans
        
        return recur(0) - 1
      