class NumArray:

    def __init__(self, nums: List[int]):
        i = 1
        while i < len(nums):
          nums[i] += nums[i - 1]
          i += 1
        self.sums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] if left == 0 else self.sums[right] - self.sums[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)