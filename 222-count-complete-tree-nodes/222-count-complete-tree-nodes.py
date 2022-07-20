# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countNodes(self, root: Optional[TreeNode]) -> int:
    cnt = 0
    def recur(node):
      if not node:
        return
      nonlocal cnt
      cnt += 1
      recur(node.left)
      recur(node.right)
    recur(root)
    return cnt