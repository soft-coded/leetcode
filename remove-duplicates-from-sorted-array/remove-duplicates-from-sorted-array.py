class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        k = len(s)
        for i in range(k):
          nums[i] = s[i]
        return k