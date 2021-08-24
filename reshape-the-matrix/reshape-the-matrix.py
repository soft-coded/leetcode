class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]): return mat
        ans = []
        nums = []
        for i in range(len(mat)):
          for j in range(len(mat[i])):
            nums.append(mat[i][j])
        ind = 0
        for i in range(r):
          row = []
          for j in range(c):
            row.append(nums[ind])
            ind += 1
          ans.append(row)
        return ans