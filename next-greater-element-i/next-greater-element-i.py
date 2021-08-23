class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      ans = []
      n = len(nums2)
      for item in nums1:
        ind = nums2.index(item)
        ng = -1
        for i in range(ind + 1, n):
          if nums2[i] > item: 
            ng = nums2[i]
            break
        ans.append(ng)
      return ans