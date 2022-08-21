class Solution:
  def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
    l = len(arr)
    for i in range(l):
      if arr[i] == 0:
        left = (i == 0) or (arr[i - 1] == 0)
        right = (i == l - 1) or (arr[i + 1] == 0)
        if left and right:
          n -= 1
          arr[i] = 1
          if n == 0:
            return True
    
    return n <= 0
    
          
        