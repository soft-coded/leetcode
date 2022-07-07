class Solution:
    def findKthLargest(self, nums, k):
        def partition(l, r):
            low = l
            while l < r:
                if nums[l] < nums[r]:
                    nums[l], nums[low] = nums[low], nums[l]
                    low += 1
                l += 1
            nums[low], nums[r] = nums[r], nums[low]
            return low
        
        l, r, k = 0, len(nums) - 1, len(nums) - k
        while True:
            pos = partition(l, r)
            if pos < k:
                l = pos + 1
            elif pos > k:
                r = pos - 1
            else:
                return nums[pos]