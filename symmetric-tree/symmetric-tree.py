# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    m = True
    def check(self, n1, n2):
      if not self.m: return
      if not n1 and not n2: return
      if (not n1) or (not n2) or (n1.val != n2.val):
        self.m = False
        return
      self.check(n1.left, n2.right)
      self.check(n1.right, n2.left)
      
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        self.m = True
        self.check(root.left, root.right)
        return self.m