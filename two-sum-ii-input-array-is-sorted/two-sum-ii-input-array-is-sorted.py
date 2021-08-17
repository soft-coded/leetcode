from bisect import bisect_left

class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        for i in range(n):
          ind = bisect_left(num, target - num[i])
          if ind < n and num[ind] == target - num[i] and ind != i:
            return [min(ind, i) + 1, max(ind, i) + 1]