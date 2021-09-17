class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
      v1 = [int(item) for item in v1.split('.')]
      v2 = [int(item) for item in v2.split('.')]
      swap = False
      if len(v1) < len(v2):
        v1, v2 = v2, v1
        swap = True
      for i in range(len(v1)):
        if (i < len(v2) and v1[i] > v2[i]) or (i >= len(v2) and v1[i] > 0):
          return -1 if swap else 1
        if i < len(v2) and v1[i] < v2[i]:
          return 1 if swap else -1
      return 0       