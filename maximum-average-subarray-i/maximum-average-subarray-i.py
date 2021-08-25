class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      n = len(nums)
      mx = -10e7
      sm = sum(nums[0:k])
      for i in range(n - k + 1):
        mx = max(sm / k, mx)
        sm -= nums[i]
        sm += nums[i + k] if i + k < n else 0
      return mx