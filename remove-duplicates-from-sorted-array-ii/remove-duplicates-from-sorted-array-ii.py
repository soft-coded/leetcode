class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      c = Counter(nums)
      ans = []
      for item in sorted(c.keys()):
        ans.extend([item] * min(c[item], 2))
      for i in range(len(ans)):
        nums[i] = ans[i]
      return len(ans)