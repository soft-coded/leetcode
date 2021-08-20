class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n1 = set(nums1)
        n2 = set(nums2)
        for item in n2:
          if item in n1:
            ans.append(item)
        return ans