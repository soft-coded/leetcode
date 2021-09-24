class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      ans = []
      for item in nums:
        if not ans or ans[-1] < item:
          ans.append(item)
        else:
          i = bisect_left(ans, item)  
          ans[i] = item
      return len(ans)
          