# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
      if not node: return 0
      l = self.height(node.left)
      r = self.height(node.right)
      if l == -1 or r == -1 or abs(l - r) > 1:
        return -1
      return max(l, r) + 1
  
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) != -1