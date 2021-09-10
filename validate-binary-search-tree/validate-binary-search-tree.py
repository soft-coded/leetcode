# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      ino = []
      def inorder(node):
        if node:
          inorder(node.left)
          ino.append(node.val)
          inorder(node.right)
      inorder(root)
      for i in range(1, len(ino)):
        if ino[i-1] == ino[i]: return False
      return ino == sorted(ino)