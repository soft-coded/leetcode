class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      c = Counter(nums)
      ans = []
      for key, val in c.items():
        if val > len(nums) // 3:
          ans.append(key)
      return ans