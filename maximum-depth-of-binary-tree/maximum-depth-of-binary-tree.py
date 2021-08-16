# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, n):
      if not n: return 0
      return max(self.height(n.left) + 1, self.height(n.right) + 1)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root)