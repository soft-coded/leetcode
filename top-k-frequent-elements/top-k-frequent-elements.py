class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      c = Counter(nums)
      items = []
      for key, val in c.items():
        items.append((val, key))
      items.sort(reverse=True)
      ans = []
      for i in range(k):
        ans.append(items[i][1])
      return ans