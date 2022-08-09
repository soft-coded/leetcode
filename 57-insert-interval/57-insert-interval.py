def merge(intv):
  intv.sort()
  lo = intv[0][0]
  hi = intv[0][1]
  ans = []
  
  for i in range(1, len(intv)):
    if hi >= intv[i][0]:
      hi = max(hi, intv[i][1])
    else:
      ans.append((lo, hi))
      lo = intv[i][0]
      hi = intv[i][1]
  
  ans.append((lo, hi))
  return ans

class Solution:
  def insert(self, intv: List[List[int]], n: List[int]) -> List[List[int]]:
    intv.append(n)
    return merge(intv)
    
    
    
    
    
    