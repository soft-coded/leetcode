from math import ceil

class Solution:
  def minSwaps(self, s: str) -> int:
    bal = 0
    for char in s:
      if char == '[':
        bal += 1
      elif bal > 0:
        bal -= 1
      
    return ceil(bal / 2)