class Solution:
    def longestConsecutive(self, nums):
        ans = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                curnum = num
                curlen = 1
                while curnum + 1 in s:
                    curnum += 1
                    curlen += 1
                ans = max(ans, curlen)
                
        return ans