# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', P: 'TreeNode', Q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None
    val = root.val
    if P.val == val or Q.val == val:
      return root
    if P.val < val < Q.val or Q.val < val < P.val:
        return root
    if P.val < val and Q.val < val:
        return self.lowestCommonAncestor(root.left, P, Q)
    return self.lowestCommonAncestor(root.right, P, Q)