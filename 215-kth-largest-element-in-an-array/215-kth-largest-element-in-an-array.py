from random import randint

def swap(arr, l, r):
  arr[l], arr[r] = arr[r], arr[l]

class Solution:
    def findKthLargest(self, nums, k):
        def partition(l, r):
            pos = randint(l, r)
            swap(nums, pos, r)
            low = l
            while l < r:
                if nums[l] < nums[r]:
                    swap(nums, l, low)
                    low += 1
                l += 1
            swap(nums, low, r)
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