class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        total = 0;
        for item in nums:
          total += abs(item - median);
        return total;