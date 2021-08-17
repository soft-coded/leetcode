class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      d = {}
      for i in range(len(nums)):
        if not d.get(nums[i]):
          d[nums[i]] = []
        d[nums[i]].append(i)
      
      for key, val in d.items():
        if len(val) > 1:
          for i in range(1, len(val)):
            if abs(val[i] - val[i - 1]) <= k:
              return True
      return False