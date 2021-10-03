class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]):
      c = Counter(arr1)
      ans = []
      for item in arr2:
        ans.extend([item] * c[item])
        del c[item]
      temp = []
      for item in c:
        temp.extend([item] * c[item])
      temp.sort()
      return ans + temp