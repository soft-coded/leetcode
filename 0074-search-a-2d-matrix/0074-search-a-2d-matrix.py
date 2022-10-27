def index(m, n, i):
  return (i // n, i % n)

class Solution:
  def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
    m = len(mat)
    n = len(mat[0])
    lo = 0
    hi = m * n - 1
    
    while lo <= hi:
      mid = (lo + hi) // 2
      mat_ind = index(m, n, mid)
      cur = mat[mat_ind[0]][mat_ind[1]]
      
      if cur == target:
        return True
      if cur > target:
        hi = mid - 1
      else:
        lo = mid + 1
    
    return False
      