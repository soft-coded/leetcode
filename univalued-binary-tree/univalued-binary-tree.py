# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
      s = set()
      def inorder(node):
        if node:
          inorder(node.left)
          s.add(node.val)
          inorder(node.right)
      inorder(root)
      return len(s) == 1