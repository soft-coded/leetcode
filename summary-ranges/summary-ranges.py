class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums: return ans
        first = cur = nums[0]
        for i in range(1, len(nums)):
          if nums[i] != cur + 1:
            if first == cur:
              ans.append(f"{cur}")
            else:
              ans.append(f"{first}->{cur}")
            first = cur = nums[i]
          else:
            cur = nums[i]
        if first == cur:
              ans.append(f"{cur}")
        else:
          ans.append(f"{first}->{cur}")
        
        return ans