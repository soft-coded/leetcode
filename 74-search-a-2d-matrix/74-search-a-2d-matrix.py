class Solution:
    def searchMatrix(self, mat: List[List[int]], t: int) -> bool:
      rows = len(mat)
      cols = len(mat[0]) - 1
      i = 0
      j = cols
      while i < rows and j >= 0:
        if mat[i][j] == t:
          return True
        elif mat[i][j] < t:
          i += 1
        else:
          j -= 1
      return False