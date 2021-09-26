# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
      pre1 = []
      pre2 = []
      def inorder(node, pre):
        if node:
          inorder(node.left, pre)
          if not node.left and not node.right:
            pre.append(node.val)
          inorder(node.right, pre)
      inorder(root1, pre1)
      inorder(root2, pre2)
      return pre1 == pre2
            