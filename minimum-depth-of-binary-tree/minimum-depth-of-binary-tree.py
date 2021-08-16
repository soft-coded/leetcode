# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def height(node):
          if not node: return 0
          if not node.left and not node.right: return 1
          if not node.left: return height(node.right) + 1
          if not node.right: return height(node.left) + 1
          return min(height(node.left), height(node.right)) + 1
        return height(root)