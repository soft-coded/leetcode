class Solution:
  def change(self, amount: int, coins: List[int]) -> int:
    memo = {}
    def recur(i, cur_am):
      if cur_am == 0:
        return 1
      if cur_am < 0 or i < 0:
        return 0
      memo_str = f"{i},{cur_am}"
      if memo_str in memo:
        return memo[memo_str]
      
      not_pick = recur(i - 1, cur_am)
      pick = recur(i, cur_am - coins[i])
      memo[memo_str] = pick + not_pick
      return memo[memo_str]
    
    return recur(len(coins) - 1, amount)