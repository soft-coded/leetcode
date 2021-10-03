class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ans = []
        for item in nums:
          if item == 0:
            ans.extend([0, 0])
          else: 
            ans.append(item)
        for i in range(len(nums)):
          nums[i] = ans[i]