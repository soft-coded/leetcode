# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
      s = set()
      def inorder(node):
        if node:
          inorder(node.left)
          s.add(node.val)
          inorder(node.right)
      inorder(root)
      for item in s:
        if k - item in s and k - item != item: return True
      return False