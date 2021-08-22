class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)
        ans = 0
        for item in nums:
          ans += item - mn
        return ans