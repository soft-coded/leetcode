class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
      cpy = sorted(nums)
      n = len(nums)
      m = (n + 1) // 2
      i, j = m - 1, 0
      while i >= 0:
        nums[j] = cpy[i]
        i -= 1
        j += 2
      i, j = n - 1, 1
      while i >= m:
        nums[j] = cpy[i]
        i -= 1
        j += 2