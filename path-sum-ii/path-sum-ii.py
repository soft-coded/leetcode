class Solution:
    def pathSum(self, root: Optional[TreeNode], ts: int) -> List[List[int]]:
      ans = []
      self.bt(ans, [], root, ts)
      return ans
    
    def bt(self, ans, path, root, ts):
      if not root: return
      if ts == root.val:
        if not root.left and not root.right:
          ans.append(path+[root.val])
          return
      self.bt(ans, path+[root.val], root.left, ts-root.val)
      self.bt(ans, path+[root.val], root.right, ts-root.val)