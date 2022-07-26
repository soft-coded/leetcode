class Solution:
  def lastStoneWeightII(self, stones: List[int]) -> int:
    sums_of_groups = {0}
    
    total = sum(stones)
    
    for weight in stones:
        addition_sums_of_groups = set()
        for sum_of_group in sums_of_groups:
            if weight + sum_of_group < total / 2:                    
                addition_sums_of_groups.add(weight + sum_of_group)
            elif weight + sum_of_group == total / 2:
                return 0
        sums_of_groups |= addition_sums_of_groups
                
    return min(abs(total - sum_of_group - sum_of_group) for sum_of_group in sums_of_groups)