class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
      ans = []
      for i in range(1, 10):
        self.dfs(i, n, ans)
      return ans
    
    def dfs(self, i, n, ans):
      if i > n: return
      ans.append(i)
      for j in range(10):
        if i * 10 + j > n: return
        self.dfs(i * 10 + j, n, ans)