class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      n = len(nums)
      k %= n
      ans = nums[n - k:] + nums[:n - k]
      for i in range(n):
        nums[i] = ans[i]