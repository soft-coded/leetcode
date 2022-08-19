class NumArray:
  def __init__(self, nums: List[int]):
    self.arr = nums
    self.seg = [-1] * (4 * len(nums))
    self._build(0, 0, len(nums) - 1)
    
  def _build(self, ind, lo, hi):
    if lo == hi:
      self.seg[ind] = self.arr[lo]
      return self.arr[lo]
    
    mid = (lo + hi) // 2
    left = self._build(2 * ind + 1, lo, mid)
    right = self._build(2 * ind + 2, mid + 1, hi)
    self.seg[ind] = left + right
    return self.seg[ind]

  def update_util(self, ind, lo, hi, i, val):
    if lo == hi:
      self.seg[ind] = val
      return
    
    mid = (lo + hi) // 2
    if i <= mid:
      self.update_util(2 * ind + 1, lo, mid, i, val)
    else:
      self.update_util(2 * ind + 2, mid + 1, hi, i, val)
    
    self.seg[ind] = self.seg[2 * ind + 1] + self.seg[2 * ind + 2]
  
  def update(self, index: int, val: int) -> None:
    return self.update_util(0, 0, len(self.arr) - 1, index, val)
  
  def sum_util(self, ind, lo, hi, l, r):
    # no overlap
    if hi < l or lo > r:
      return 0
    # complete overlap
    if lo >= l and hi <= r:
      return self.seg[ind]
    
    mid = (lo + hi) // 2
    left = self.sum_util(2 * ind + 1, lo, mid, l, r)
    right = self.sum_util(2 * ind + 2, mid + 1, hi, l, r)
    return left + right
    
    
  def sumRange(self, left: int, right: int) -> int:
    return self.sum_util(0, 0, len(self.arr) - 1, left, right)    


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)