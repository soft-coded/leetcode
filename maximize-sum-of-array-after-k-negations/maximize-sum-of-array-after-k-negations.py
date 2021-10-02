class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
      heapq.heapify(nums)
      for _ in range(k):
          heapq.heappush(nums, -heapq.heappop(nums))
      return sum(nums)
      