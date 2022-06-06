class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = set(), set()
        for i in range(len(mat)):
          for j in range(len(mat[0])):
            if mat[i][j] == 0:
              rows.add(i)
              cols.add(j)
              
        for row in rows:
          for col in range(len(mat[0])):
            mat[row][col] = 0
          
        for col in cols:
          for row in range(len(mat)):
            mat[row][col] = 0