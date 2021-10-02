# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
      sm = 0
      def inorder(node):
        if node:
          inorder(node.left)
          if low <= node.val <= high:
            nonlocal sm
            sm += node.val
          inorder(node.right)
      inorder(root)
      return sm