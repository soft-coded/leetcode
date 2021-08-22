class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        return nums[-3] if len(nums) > 2 else nums[-1]