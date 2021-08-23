class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ans = []
      d = {}
      n = len(nums2)
      for i in range(n):
        d[nums2[i]] = i
      for item in nums1:
        ng = -1
        for i in range(d[item] + 1, n):
          if nums2[i] > item: 
            ng = nums2[i]
            break
        ans.append(ng)
      return ans