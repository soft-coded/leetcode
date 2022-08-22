# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def is_sorted(arr):
#   for i in range(1, len(arr)):
#     if arr[i] <= arr[i - 1]:
#       return False
#   return True

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def traverse(node, l, r):
      if not node:
        return True
      if not (l < node.val < r):
        return False
      
      left = traverse(node.left, l, node.val)
      right = traverse(node.right, node.val, r)
      
      return left and right
    
    return traverse(root, -math.inf, math.inf)
      
      
      
      