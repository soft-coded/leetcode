class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        
        for num in nums:
            if num - 1 not in s:
                nn = num
                curlen = 1
                while nn + 1 in s:
                    curlen += 1
                    nn += 1
                
                ans = max(ans, curlen)
        
        return ans