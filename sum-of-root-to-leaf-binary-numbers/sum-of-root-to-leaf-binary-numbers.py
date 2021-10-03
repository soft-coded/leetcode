# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
      sm = 0
      def inorder(node, path):
        if node:
          val = str(node.val)
          inorder(node.left, path + val)
          if not node.left and not node.right:
            nonlocal sm
            sm += int(path + val, 2)
            return
          inorder(node.right, path + val)
      inorder(root, "")
      return sm