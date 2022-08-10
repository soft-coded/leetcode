def is_same(n1, n2):
  if not n1 and not n2: return True
  if not n1 or not n2: return False
  if n1.val != n2.val: return False
  return is_same(n1.left, n2.left) and is_same(n1.right, n2.right)

class Solution:
    def isSubtree(self, r: Optional[TreeNode], sr: Optional[TreeNode]) -> bool:
      if not r: return False
      if is_same(r, sr): return True
      return self.isSubtree(r.left, sr) or self.isSubtree(r.right, sr)