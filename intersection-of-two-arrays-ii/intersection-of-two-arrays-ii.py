from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        ans = []
        for item in n1.keys():
          if n2.get(item):
            mn = min(n1[item], n2[item])
            i = 0
            while i < mn:
              ans.append(item)
              i += 1
        return ans