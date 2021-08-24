# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        s = 0
        def sm(node):
          nonlocal s
          if not node: return 0
          l = sm(node.left)
          r = sm(node.right)
          s += abs(l - r)
          return l + r + node.val
        sm(root)
        return s