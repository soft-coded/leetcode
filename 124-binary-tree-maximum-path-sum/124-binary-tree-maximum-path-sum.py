# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      self.ans = -math.inf
      
      def path_sum(node):
        if not node:
          return 0
        
        l = max(0, path_sum(node.left))
        r = max(0, path_sum(node.right))
        sm = l + r + node.val
        self.ans = max(self.ans, sm)
        return node.val + max(l, r)
      
      path_sum(root)
      return self.ans