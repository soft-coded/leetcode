class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      d = Counter(nums)
      ans = [0, 0]
      for i in range(1, len(nums) + 1):
        if not d.get(i): ans[1] = i
        elif d.get(i) > 1: ans[0] = i
        if ans[0] and ans[1]: return ans