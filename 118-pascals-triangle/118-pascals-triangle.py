class Solution:
    def generate(self, n: int) -> List[List[int]]:
      if n == 1: return [[1]]
      ans = [[1], [1, 1]]
      if n == 2: return ans
      for i in range(2, n):
        row = [1]
        for j in range(1, i):
          row.append(ans[i-1][j-1] + ans[i-1][j])
        row.append(1)
        ans.append(row)
      return ans