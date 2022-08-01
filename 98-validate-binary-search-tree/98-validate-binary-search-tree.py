# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def is_sorted(arr):
  for i in range(1, len(arr)):
    if arr[i] <= arr[i - 1]:
      return False
  return True

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    ino = []
    def inorder(node):
      if not node:
        return
      inorder(node.left)
      ino.append(node.val)
      inorder(node.right)
      
    inorder(root)
    return is_sorted(ino)