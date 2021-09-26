class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
      tr = []
      for i in range(len(mat[0])):
        row = []
        for j in range(len(mat)):
          row.append(mat[j][i])
        tr.append(row)
      return tr