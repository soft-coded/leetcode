class Solution:
    def maxSubArray(self, a: List[int]) -> int:
      all_max = max_till_here = a[0]
      for i in range(1, len(a)):
        max_till_here = max(max_till_here + a[i], a[i])
        all_max = max(all_max, max_till_here)
      return all_max