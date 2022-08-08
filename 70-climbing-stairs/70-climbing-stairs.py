class Solution:
  def climbStairs(self, n: int) -> int:
    memo = {}
    def recur(i):
      if i == 0:
        return 1
      if i < 0:
        return 0
      if i in memo:
        return memo[i]
      
      one = recur(i - 1)
      two = recur(i - 2)
      memo[i] = one + two
      return memo[i]
    
    return recur(n)