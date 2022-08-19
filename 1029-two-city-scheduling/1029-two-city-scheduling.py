class Solution:
  def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    diff = [j - i for i, j in costs]
    diff.sort()
    total = 0
    for i, _ in costs:
      total += i
    
    for i in range(len(costs) // 2):
      total += diff[i]
    
    return total