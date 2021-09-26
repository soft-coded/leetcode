# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
      cur = dummy = TreeNode()
      def inorder(node):
        nonlocal cur
        if node:
          inorder(node.left)
          cur.right = cur = TreeNode(node.val)
          inorder(node.right)
      inorder(root)
      return dummy.right