class RecentCounter:

    def __init__(self):
      self.reqs = []

    def ping(self, t: int) -> int:
      self.reqs.append(t)
      i = len(self.reqs) - 1
      cnt = 0
      while i > -1 and t - self.reqs[i] <= 3000:
        cnt += 1
        i -= 1
      return cnt

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)