class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
      if len(arr) < 3: return False
      i = 0
      while i < len(arr) - 1 and arr[i + 1] > arr[i]:
        i += 1
      j = i + 1
      while j < len(arr) and arr[j] < arr[j - 1]:
        j += 1
      return 0 < i < len(arr) - 1 and j == len(arr)