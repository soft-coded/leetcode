def count01(s):
  zeros = ones = 0
  for char in s:
    if char == '1':
      ones += 1
    else:
      zeros += 1
  return zeros, ones

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      
      def recur(index, cur_m, cur_n, memo):
        if index == len(strs) or (cur_m < 0 or cur_n < 0) or (cur_m == 0 and cur_n == 0):
          return 0
        
        memo_str = f"{index},{cur_m},{cur_n}"
        if memo_str in memo:
          return memo[memo_str]
        
        not_pick = recur(index + 1, cur_m, cur_n, memo)
        zeros, ones = count01(strs[index])
        pick = -math.inf
        if zeros <= cur_m and ones <= cur_n:
          pick = 1 + recur(index + 1, cur_m - zeros, cur_n - ones, memo)
        
        ans = max(not_pick, pick)
        memo[memo_str] = ans
        return ans
      
      return recur(0, m, n, {})
        
        
        
        
        
        
        
        
        
        
        
        
        