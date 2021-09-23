class Solution:
  def productExceptSelf(self, nums):
    p = 1
    n = len(nums)
    ans = []
    for i in range(n):
      ans.append(p)
      p *= nums[i]
    p = 1
    for i in range(n-1, -1, -1):
      ans[i] *= p
      p *= nums[i]
    return ans