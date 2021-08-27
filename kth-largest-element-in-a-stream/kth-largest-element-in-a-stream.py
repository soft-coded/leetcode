class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      self.sn = sorted(nums)
      self.k = -k

    def add(self, val: int) -> int:
      ind = bisect_left(self.sn, val)
      self.sn.insert(ind, val)
      return self.sn[self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)